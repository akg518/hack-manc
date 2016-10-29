from flask import Flask, jsonify, render_template, request
# from concept import Concept
# from NLP import getStringInfo
# from chatroom import *

app=Flask(__name__)

# @app.route('/_get_suggestions_')
# def get_suggestions():
#   input_text = request.args.get('input_text', '', type=string)
#   if input_text = ""
#     return
#   input_concept = Concept()
#   input_concept.importFromJSON(getStringInfo(input_text))
#   return jsonify(result=input_concept.top5chatrooms)

# @app.route('/_pull_data_')
# def pull_data():
#   uid = request.args.get('uid', '', type=string)
#   return jsonify (result=CHATROOMS[uid].get_text())

# @app.route('/_make_new_chatroom_')
# def make_new_chatroom():
#   global CHATROOMS
#   concept_string = request.args.get('concept_string', '', type=string)
#   username = request.args.get('username', '', type=string)
#   user_ip = request.args.get('user_ip', '', type=string)
#   new_concept = Concept()
#   new_concept.importFromJSON(concept_string)
#   uid = createNewChatroom(concept)
#   CHATROOMS[uid].add_user(username, user_ip)
#   return jsonify(result=uid)

# @app.route('/_add_user_to_chatroom')
# def add_user_to_chatroom():
#   global CHATROOMS
#   uid = request.args.get('uid', '', type=string)
#   username = request.args.get('username', '', type=string)
#   user_ip = request.args.get('user_ip', '', type=string)
#   CHATROOMS[uid].add_user(username, user_ip)

# @app.route('/_add_text_to_chatroom_')
# def add_text_to_chatroom():
#   global CHATROOMS
#   uid = request.args.get('chatroom_uid', '', string) # chatroom id
#   user_ip = request.args.get('user_ip', '', string) # user ip
#   entry = request.args.get('entry', '', string) # text to enter
#   username = CHATROOMS[uid].get_user(user_ip)
#   CHATROOMS[uid].add_entry(username, entry)

@app.route('/hello_world')
def hello_world():
  return jsonify(result="hello world")

@app.route('/check_param')
def check_param():
  param = request.args.get('param_id', '', string)
  return jsonify(result = "SERVER RESPONSE: " + param)  
  
@app.route('/')
def index():
  return render_template('main.html')
  
@app.route('/chatroom/<uid>')
def chatroom(uid):
  return render_template('chatroom.html', uid=uid)

