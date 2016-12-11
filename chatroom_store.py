"""
module that handles all the logic of managing chatroom data.
Managing chatroom data includes creating new chatrooms, deleting unused chatrooms, validating integrity,
updating the chatroom concept data and reviewing current users.

The data will be stored according to (possibly multiple) specifications.
Currently chatrooms are only stored in memory. Later they will be saved as JSON files on the webstore, or as a db.
"""

import conf
from chatroom import Chatroom
from concept import Concept
import jsonpickle
from datetime import datetime

class ChatroomStore:
    def __init__(self):
        conf.v_print("setting up chatrooms...")
        self.lastUpdateTime = datetime.now()
        self.chatrooms = {}  # maps uid to chatroom object or to None if not cached

        # maps uid to concept objects of the chatroom. All concepts are stored in memory for search purposes!
        self.concepts = {}

        if conf.FILESTORE:
            if conf.FILE_STORAGE_TYPE == 'JSON':
                pass


    def load_chatrooms_from_JSON(self, filename):
        """
        Loads saved chatrooms from JSON file and appends it to the current chatroom list.
        :param filename: filename of the JSON dump
        :return: None
        """
        #TODO add some cache capacity constraints
        f = open(filename, 'r')
        jsondict = jsonpickle.decode(f.read())
        for key in jsondict:
        if type(jsondict[key]) is dict:
            self.chatrooms[key]=Chatroom.fromDict(jsondict[key])
            self.chatrooms[key].concept = Concept.fromDict(self.chatrooms[key].concept)
            self.concepts[key] = self.chatrooms[key].concept
        else:
          chatroomList[key]=jsondict[key]
        f.close()

        def add_chatroom(chatroom, uid=None):
            """
            Adds a new chatroom or overrides an old one.
            :param chatroom: a chatroom object.
            :param key: unique identifier used to associate with the object.
                If equal to none then new non-overriding key will be generated.
            :return: None
            """
