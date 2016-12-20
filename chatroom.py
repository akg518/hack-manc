import random
import jsonpickle
from concept import Concept

TEST_CHATROOMS = {}
CHATROOM_DATA = ["it is pretty rainy today, I don't want to go outside",
                 "I wander what to eat for lunch - maybe some stir fry?",
                 "I want new cook up some new recipes.",
                 "it's a really nice weather today - I should go outside and play in the park!",
                 "camembert cheese is the best cheese",
                 "I'm tired, I need to get some fresh air",
                 "It's really cold outside, I should buy a new jacket",
                 "what is the best type of coffee?",
                 "that chocolate from coop is really good!",
                 "which country has the best weather?",
                 "I need more caffeine - I'm so tired!",
                 "Today's tuna sandwitches were really nice!",
                 "Does anyone know where I can get fresh cucamber",
                 "I hate when my jeans are too tight",
                 "I have found a fantastic pizza place in my neighbourhood",
                 "It's important to wear matching pairs of clothing",
                 "How can people add pickles to salads?!",
                 "I'm trying to save up for the new pair of shoes",
                 "do you think it always rains in scotland?",
                 "I'm looking for a substitue for bread, I really need to go on diet"]
CHATROOM_DATA_UPDATE = False

class Chatroom(object):
    def __init__(self, concept):
      self.concept = concept
      self.users = {}  # written as ip:username (for now)
      self.entries = []  # written as [(user, text)]

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
        checks the staus of each user connection, drops out people no longer found
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

    def getTopWords(self):
        chat_markers = self.concept.keywords.items()
        chat_markers.extend([(topic[0][topic[0].rfind('/')+1:], topic[1]) for topic in self.concept.topics.items()]) # create markers with the most important categories and score
        top3 = sorted(chat_markers, key = lambda x: x[1], reverse=True)
        top3 = top3[:min(3, len(top3))]
        top3 = [entry[0] for entry in top3]
        result = "Let us chat about " + ', '.join(top3[:-1]) + " and " + top3[-1]
        return result

    @staticmethod
    def fromDict(dicitonary):
      result = Chatroom(None, None)
      result.__dict__ = dicitonary
      if type(result.concept) is dict:
          result.concept = Concept.fromDict(result.concept)
      return result
      


  

  
if __name__=="__main__":
    # if CHATROOM_DATA_UPDATE:
    #   createTempChatrooms(CHATROOM_DATA, TEST_CHATROOMS)
    #   saveCurrentChatrooms("dumps.json", TEST_CHATROOMS)
    # loadChatrooms("dumps.json", TEST_CHATROOMS)
    # print TEST_CHATROOMS['991'].getTopWords()
    #   compare_concept=Concept()
    #   compare_concept.importFromText("this weather sucks - it is far too rainy! I would far prefer if it was sunny.")
    #   #compare_concept.top5chatrooms(TEST_CHATROOMS)
    #   uid = createNewChatroom(compare_concept, TEST_CHATROOMS)
    #   TEST_CHATROOMS[uid].getTopWords()
    pass
  
  
  
  


