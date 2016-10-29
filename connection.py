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


@app.route('_add_to_chatroom_')
def add_to_chatroom():
  chatroom_name = request.args.get('chatroom_uid')
  