"""
module that handles all the logic of managing chatroom data.
Managing chatroom data includes creating new chatrooms, deleting unused chatrooms, validating integrity,
updating the chatroom concept data and reviewing current users.

The data will be stored according to (possibly multiple) specifications.
Currently chatrooms are only stored in memory. Later they will be saved as JSON files on the webstore, or as a db.
"""

import conf
from chatroom import Chatroom
import jsonpickle
from datetime import datetime
import random
import string

class ChatroomStore:
    def __init__(self):
        conf.v_print("setting up chatrooms...")
        self.lastUpdateTime = datetime.now()
        self.chatrooms = {}  # type: dict[string, Chatroom]
        self.total_users = 0  # total users across all chatrooms

        if conf.FILESTORE:
            if conf.FILE_STORAGE_TYPE == 'JSON':
                pass

    def load_chatrooms_from_JSON(self, filename):
        """
        Loads saved chatrooms from JSON file and appends it to the current chatroom list.
        :param filename: filename of the JSON dump
        :return: None
        """
        f = open(filename, 'r')
        jsondict = jsonpickle.decode(f.read())
        for key in jsondict:
            if type(jsondict[key]) is dict:
                temp_chatroom = Chatroom.fromDict(jsondict[key])
                self.add_chatroom(temp_chatroom)
            else:
                self.add_chatroom(jsondict[key])
        f.close()

    def save_chatrooms_to_JSON(self, filename):
        #TODO check if I even work
        f = open(filename, 'w')
        f.write(jsonpickle.encode(self.chatrooms))
        f.close()


    def add_chatroom(self, chatroom, key=None):
        """
        Adds a new chatroom or overrides an old one.
        :param chatroom: a chatroom object.
        :param key: unique identifier used to associate with the object.
            If equal to none then new non-overriding key will be generated.
        :return: uid of the new chatroom
        """
        # generate a random key
        if key is not None:
            uid = str(key)
        else:
            uid = ''.join(random.choice(string.digits + string.letters) for _ in xrange(6))
            while uid in self.chatrooms.keys():
                uid = ''.join(random.choice(string.digits + string.letters) for _ in xrange(6))
        # adding the chatroom
        self.chatrooms[uid] = chatroom
        conf.v_print("chatroom added successfully!")
        return uid

    def get_chatroom_keys(self):
        """
        gets a list of all chatroom unique identifiers
        """
        return self.chatrooms.keys()

    def update_users(self):
        """
        updates the current amount of users of the chatroom (checking if users dropped off etc.)
        """
        new_user_count = 0
        for chatroom in self.chatrooms:
            chatroom.update_users()
            new_user_count += chatroom.get_total_users()
        self.total_users = new_user_count

    def add_user(self, uid, user_ip, user_name):
        if self.chatrooms[uid].add_user(user_name, user_ip):
            self.total_users += 1
            conf.v_print("user " + user_name + " added successfully")
        else:
            conf.v_print("adding of user " + user_name + "unsuccessful...")

    def validate_uid(self, uid):
        if uid not in self.chatrooms():
            raise AssertionError("Chatroom does not exist!")

    def get_text(self, uid):
        """
        get text for the chatroom
        :param uid: unique identifier string of the chatroom
        :return: string block to be printed
        """
        self.validate_uid(uid)
        return self.chatrroms[uid].get_text()

    def add_text(self, uid, user_ip, text):
        """
        add text to the chatroom. Raise upon error.
        :param uid: unique identifier string of the chatroom
        :param user_ip: user ip
        :param text: text to be inserted
        """
        self.validate_uid(uid)
        username = self.chatrooms[uid].get_user(user_ip)
        self.chatrooms[uid].add_entry(username, text)

    def get_title(self, uid):
        """
        gets title of the chatroom. Raise upon Error
        """
        self.validate_uid(uid)
        return self.chatrooms[uid].get_title()