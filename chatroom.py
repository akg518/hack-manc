import random
import jsonpickle
from concept import Concept


class Chatroom(object):
    def __init__(self, concept):
        self.concept = concept
        self.users = {}  # written as ip:username (for now)
        self.entries = []  # written as [(user, text)]
        self.title = self.generateTitle()

    def getText(self):
        #TODO fix this, html tags should not exist in a concept entity but in an html rendering entity
        return '</br>'.join(['<strong>'+row[0]+'</strong>: '+row[1] for row in self.entries])

    def add_user(self, username, user_ip):
        """
        Adds a user to the chatroom.
        :param username: username
        :param user_ip: user ip
        :return: Boolean. Success status.
        """
        #TODO check validation if user already in the chatroom
        self.users[user_ip] = username
        return True
       
    def get_user(self, user_ip):
        return self.users[user_ip]

    def update_users(self):
        """
        checks the status of each user connection, drops out people no longer found
        """
        pass

    def get_total_users(self):
        """
        get the total amount of users in the chatroom
        """
        return self.users

    def add_entry(self, user, text):
        self.entries.append((user, text))
        if len(self.entries) > 20:
            self.entries = self.entries[-20:]

    def generateTitle(self):
        chat_markers = self.concept.keywords.items()
        chat_markers.extend([(topic[0][topic[0].rfind('/')+1:], topic[1]) for topic in self.concept.topics.items()]) # create markers with the most important categories and score
        top3 = sorted(chat_markers, key = lambda x: x[1], reverse=True)
        top3 = top3[:min(3, len(top3))]
        top3 = [entry[0] for entry in top3]
        result = "Let us chat about " + ', '.join(top3[:-1]) + " and " + top3[-1]
        return result

    def get_title(self):
        return self.title

    @staticmethod
    def fromDict(dicitonary):
      result = Chatroom(None, None)
      result.__dict__ = dicitonary
      if type(result.concept) is dict:
          result.concept = Concept.fromDict(result.concept)
      return result
      

  
  
  
  


