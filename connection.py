from flask import Flask, jsonify, render_template, request
from chatroom import *
from concept import Concept
import jsonpickle
# from NLP import getStringInfo
# from chatroom import *

app=Flask(__name__)

SERVER_CHATROOMS= {}

SETUP_FLAG = False


def setup():
  global SETUP_FLAG
  global SERVER_CHATROOMS
  loadChatrooms("dumps.json", SERVER_CHATROOMS)
  SETUP_FLAG = True
  

@app.route('/_get_suggestions_')
def get_suggestions():
  input_text = request.args.get('input_text', '', type=str)
  if input_text == "":
    return ""
  input_concept = Concept()
  input_concept.importFromText(input_text)
  suggestion_list = input_concept.top5chatrooms(SERVER_CHATROOMS)
  tempResult = [(SERVER_CHATROOMS[entry[0]].getTopWords(), entry[1]) for entry in suggestion_list]
  print tempResult
  return jsonify(result=tempResult)

@app.route('/_pull_data_')
def pull_data():
  uid = request.args.get('uid', '', type=str)
  return jsonify (result=SERVER_CHATROOMS[uid].get_text())

@app.route('/_make_new_chatroom_')
def make_new_chatroom():
  global SERVER_CHATROOMS
  concept_string = request.args.get('concept_string', '', type=str)
  username = request.args.get('username', '', type=str)
  user_ip = request.args.get('user_ip', '', type=str)
  new_concept = Concept()
  new_concept.importFromText(concept_string)
  uid = createNewChatroom(concept)
  SERVER_CHATROOMS[uid].add_user(username, user_ip)
  return jsonify(result=uid)

# @app.route('/_add_user_to_chatroom')
# def add_user_to_chatroom():
#   global CHATROOMS
#   uid = request.args.get('uid', '', type=string)
#   username = request.args.get('username', '', type=str)
#   user_ip = request.args.get('user_ip', '', type=str)
#   CHATROOMS[uid].add_user(username, user_ip)

@app.route('/_add_text_to_chatroom_')
def add_text_to_chatroom():
  global CHATROOMS
  uid = request.args.get('uid', '', type=str) # chatroom id
  user_ip = request.args.get('user_ip', '', type=str) # user ip
  entry = request.args.get('entry', '', type=str) # text to enter
  return jsonify(result = "SERVER uid: " + uid +"\nuserip: " + user_ip +"\nentry: " + entry);
  #username = CHATROOMS[uid].get_user(user_ip)
  #CHATROOMS[uid].add_entry(username, entry)

@app.route('/hello_world')
def hello_world():
  return jsonify(result="heb world")

@app.route('/check_param')
def check_param():
  param = request.args.get('param', '', type=str)
  return jsonify(result = "SERVER RESPONSE: " + param)  
  
@app.route('/')
def index():
  if not SETUP_FLAG:
    setup()
  return render_template('main.html')
  
@app.route('/chatroom/<uid>')
def chatroom(uid):
  return render_template('chatroom.html', uid=uid, chatroom_ids = SERVER_CHATROOMS.keys())

