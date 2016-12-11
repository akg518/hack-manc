"""
server module

contatins all the server related functions
i.e website rendering, jquery dynamic handlers etc.
currently it is storing all the chatrooms in memory
"""

# TODO create a proper chatroom management structure - use buffer and garbage collect unused chatrooms
# TODO fix the chatroom implementation - USE callback funcitons rather than probing!

from flask import Flask, jsonify, render_template, request
from chatroom import *
from concept import Concept
from optparse import OptionParser
import conf

app = Flask(__name__)

SERVER_CHATROOMS= {}

def init_server():
    """
    initializes the server, declares all the constants in the config file
    """
    # parsing command line flags
    parser = OptionParser()
    parser.add_option('-f', '--filestore', action='store_true', dest="filestore", default=False,
                      help="determines whether the chatrooms are stored in filestore or kept dynamically")
    parser.add_option('-v', '--verbose', action='store_true', dest="verbose", default=False,
                      help="makes server output more verbose")
    parser.add_option('-d', '--debug', action='store_true', dest="debug", default=False,
                      help="adds a debug flag to the server, look flask server debug mode for more details")
    (options, args) = parser.parse_args()
    conf.setup_globals(options.debug, options.verbose, options.filestore)

    # loading chatrooms from file
    if conf.FILESTORE:
        global SERVER_CHATROOMS
        loadChatrooms("dumps.json", SERVER_CHATROOMS)

    if conf.VERBOSE:
        print "server setup complete"

def update_loop():
    """
    update loop should run in a separate thread
    in here are defined all the standard non-http related server tasks
    eg. regular cache writeback, consistency validation etc.
    Also in here concept structure for chatrooms will be periodically updated
    """
    pass


@app.route('/_get_suggestions_')
def get_suggestions():
    """
    JQUERY REQUEST
    get suggestions for a given input string
    input string will be analyzed and compared against all the chatrooms (needs to be changed)
    :return: list of suggestions in JSON format: [(top_words_for_chatroom, relevance, uid)]
    """
    input_text = request.args.get('input_text', '', type=str)

    if conf.VERBOSE:
        print "getting suggestions for input: " + input_text

    if input_text == "":
        return ""
    input_concept = Concept()
    input_concept.importFromText(input_text)
    suggestion_list = input_concept.top5chatrooms(SERVER_CHATROOMS)
    tempResult = [(SERVER_CHATROOMS[entry[0]].getTopWords(), entry[1], entry[0]) for entry in suggestion_list]
    if conf.VERBOSE:
        print "top results:"
        for i, item in enumerate(tempResult):
            print str(i)+": "+str(item)
    return jsonify(result=tempResult)

@app.route('/_pull_data_')
def pull_data():
    """
    JQUERY REQUEST
    gets text data for a given chatroom.
    :return: JSON format of chatroom text
    """
    uid = request.args.get('uid', '', type=str)
    return jsonify(result=SERVER_CHATROOMS[uid].getText())

@app.route('/_make_new_chatroom_')
def make_new_chatroom():
    """
    creates a new chatroom and adds a creator user to it
    :return: the id of the new website (soon to be the new website to be rendered)
    """
    #TODO fix this function, use flask to redirect to the website and not javascript!
    global SERVER_CHATROOMS
    concept_string = request.args.get('concept_string', '', type=str)
    username = request.args.get('username', '', type=str)
    user_ip = request.args.get('user_ip', '', type=str)
    new_concept = Concept()
    new_concept.importFromText(concept_string)
    uid = createNewChatroom(new_concept)
    SERVER_CHATROOMS[uid].add_user(username, user_ip)
    return jsonify(result=uid)


@app.route('/_add_user_to_chatroom')
def add_user_to_chatroom():
    """
    adds a user to the chatroom
    either returns an error message or redirects to the correct page
    """
    global SERVER_CHATROOMS
    uid = request.args.get('uid', '', type=str)
    username = request.args.get('username', '', type=str)
    user_ip = request.args.get('user_ip', '', type=str)
    SERVER_CHATROOMS[uid].add_user(username, user_ip)
    return jsonify(result="success!")


@app.route('/_add_text_to_chatroom_')
def add_text_to_chatroom():
    """
    adds user message to the server store.
    """
    # TODO: here method will use will callback the recipients of the message.
    global SERVER_CHATROOMS
    uid = request.args.get('uid', '', type=str) # chatroom id
    user_ip = request.args.get('user_ip', '', type=str) # user ip
    entry = request.args.get('entry', '', type=str) # text to enter
    if user_ip not in SERVER_CHATROOMS[uid].users:
        SERVER_CHATROOMS[uid].add_user("anonymous", "user_ip")
    username = SERVER_CHATROOMS[uid].get_user(user_ip)
    SERVER_CHATROOMS[uid].add_entry(username, entry)
    return jsonify(result="success!")


@app.route('/')
def index():
    """
    render the main website
    """
    return render_template('main.html')


@app.route('/chatroom/<uid>')
def chatroom(uid):
    """
    renders the chatroom webpage
    :param uid:
    """
    title = request.args.get('title', '', type=str)
    return render_template('chatroom.html', uid=uid, title=title, chatroom_ids = SERVER_CHATROOMS.keys())

if __name__ == "__main__":
    init_server()
    app.run(host='127.0.0.1', port=5000)
