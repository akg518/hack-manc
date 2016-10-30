from flask import Flask, jsonify, render_template, request
from chatroom import *
# from NLP import getStringInfo
# from chatroom import *

app=Flask(__name__)

SETUP_FLAG = False

def setup():
  global SETUP_FLAG
  loadChatrooms("dumps.json")
  SETUP_FLAG = True
  

@app.route('/_get_suggestions_')
def get_suggestions():
  input_text = request.args.get('input_text', '', type=str)
  if input_text == "":
    return ""
  input_concept = Concept()
  input_concept.importFromText(input_text)
  return jsonify(result=input_concept.top5chatrooms(CHATROOMS))

# @app.route('/_pull_data_')
# def pull_data():
#   uid = request.args.get('uid', '', type=str)
#   return jsonify (result=CHATROOMS[uid].get_text())

# @app.route('/_make_new_chatroom_')
# def make_new_chatroom():
#   global CHATROOMS
#   concept_string = request.args.get('concept_string', '', type=string)
#   username = request.args.get('username', '', type=str)
#   user_ip = request.args.get('user_ip', '', type=str)
#   new_concept = Concept()
#   new_concept.importFromJSON(concept_string)
#   uid = createNewChatroom(concept)
#   CHATROOMS[uid].add_user(username, user_ip)
#   return jsonify(result=uid)

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
  return render_template('chatroom.html', uid=uid)

