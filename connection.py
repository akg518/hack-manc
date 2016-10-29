from flask import Flask, jsonify, render_template, request
from concept import Concept
from NLP import getStringInfo
from chatroom import *

app=Flask(__name__)

@app.route('/_get_suggestions_')
def get_suggestions():
  input_text = request.args.get('input_text', '', type=string)
  if input_text = ""
    return
  input_concept = Concept()
  input_concept.importFromJSON(getStringInfo(input_text))
  return jsonify(result=input_concept.top5chatrooms)

@app.route('/_pull_data_')
def pull_data():
  uid = request.args.get('uid', '', type=string)
  return jsonify (result=CHATROOMS[uid].get_text())


@app.route('/_add_to_chatroom_')
def add_to_chatroom():
  chatroom_name = request.args.get('chatroom_uid')
  return jsonify(result="hello world")


  
  
@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/chatroom/<uid>')
def chatroom(uid):
  return render_template('chatrom.html', uid=uid)

