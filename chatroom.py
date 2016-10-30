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
                 "I'm looking for a substitue for bread, I really need to go on diet",
#                  "Black clothes make me look fat",
#                  "I have tried the best salami and cheese sandwich ever",
#                  "It's been a while since I had a soup",
#                  "Off for a sunday dinner with family",
#                  "What should I wear for a formal dinner with my work team",
#                  "People shouldn't wear black ties with black shirts"
                ]
CHATROOM_DATA_UPDATE = False

class Chatroom(object):
    def __init__(self, uid, concept):
      self.uid=uid
      self.concept = concept
      self.users = {}
      self.entries = [] # [(user, text)] 

    def getText(self):
        return '\n'.join([': '.join(row) for row in self.entries])

    def add_user(self, username, user_ip):
        #TODO check validation if user already in the chatroom
        self.users[user_ip] = username
       
    def get_user(self, user_ip):
        return self.users[user_ip]

    def add_entry(self, user, text):
        self.entries.append((user, text))
        if len(self.entries) > 20:
            self.entries = self.entries[-20:]

    def getTopWords(self):
        key2 = sorted(self.concept.keywords.items(), key=lambda x: x[1])
        result = "chat about "
        for keyNum in xrange(len(key2)):
          result += ", " + str(key2[-1*keyNum][0])
          if keyNum==3:
            break
        return str(result)

    def get_uid(self):
        return self.uid

    @staticmethod
    def fromDict(dicitonary):
      result = Chatroom(None, None)
      result.__dict__ = dicitonary
      return result
      

def createNewChatroom(concept, chatroomList):
    uid = ""
    while True:
        uid =str(random.randint(0, 100000))
        if uid not in chatroomList.keys():
            new_chatroom = Chatroom(uid, concept)
            chatroomList[uid]=new_chatroom
            break
    return uid

def createTempChatrooms(chatroom_data):
  for input_string in chatroom_data:
    new_concept = Concept()
    new_concept.importFromText(input_string)
    createNewChatroom(new_concept)
    
def saveCurrentChatrooms(filename, chatroomList):
  f = open(filename, 'w')
  f.write(jsonpickle.encode(chatroomList))
  f.close()
  
def loadChatrooms(filename, chatroomList):
  print "chatroom class here!"
  chatroomList.clear()
  f = open(filename, 'r')
  jsondict = jsonpickle.decode(f.read())
  for key in jsondict:
    #print str(key)+  ": " + str(jsondict[key])
    print type(jsondict[key])
    if type(jsondict[key]) is dict:
      chatroomList[key]=Chatroom.fromDict(jsondict[key])
      chatroomList[key].concept = Concept.fromDict(chatroomList[key].concept)
    else:
      chatroomList[key]=jsondict[key]
  print "chatroom lenght:" + str(len(chatroomList))
  for key in chatroomList:
    print key
    print chatroomList[key].concept
  f.close()
  
if __name__=="__main__":
  if CHATROOM_DATA_UPDATE:
    createTempChatrooms(CHATROOM_DATA, TEST_CHATROOMS)
    saveCurrentChatrooms("dumps.json", TEST_CHATROOMS)
  loadChatrooms("dumps.json", TEST_CHATROOMS)
  compare_concept=Concept()
  compare_concept.importFromText("this weather sucks - it is far too rainy!")
  print compare_concept.top5chatrooms(TEST_CHATROOMS)
  
  
  


