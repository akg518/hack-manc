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
        print self.users
        return self.users[user_ip]

    def add_entry(self, user_ip, text):
        self.entries.append((self.get_user(user_ip), text))
        if len(self.entries) > 20:
            self.entries = self.entries[-20:]

    def getTopWords(self):
        chat_markers = self.concept.keywords.items()
        chat_markers.extend([(topic[0][topic[0].rfind('/')+1:], topic[1]) for topic in self.concept.topics.items()]) # create markers with the most important categories and score
        top3 = sorted(chat_markers, key = lambda x: x[1], reverse=True)
        top3 = top3[:min(3, len(top3))]
        top3 = [entry[0] for entry in top3]
        result = "Let's chat about " + ', '.join(top3[:-1]) + " and " + top3[-1]
        return result
      
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

def createTempChatrooms(chatroom_data, chatroomList):
  for input_string in chatroom_data:
    new_concept = Concept()
    new_concept.importFromText(input_string)
    createNewChatroom(new_concept, chatroomList)
    
def saveCurrentChatrooms(filename, chatroomList):
  f = open(filename, 'w')
  f.write(jsonpickle.encode(chatroomList))
  f.close()
  
def loadChatrooms(filename, chatroomList):
  chatroomList.clear()
  f = open(filename, 'r')
  jsondict = jsonpickle.decode(f.read())
  for key in jsondict:
    if type(jsondict[key]) is dict:
      chatroomList[key]=Chatroom.fromDict(jsondict[key])
      chatroomList[key].concept = Concept.fromDict(chatroomList[key].concept)
    else:
      chatroomList[key]=jsondict[key]
  f.close()
  
if __name__=="__main__":
  if CHATROOM_DATA_UPDATE:
    createTempChatrooms(CHATROOM_DATA, TEST_CHATROOMS)
    saveCurrentChatrooms("dumps.json", TEST_CHATROOMS)
  loadChatrooms("dumps.json", TEST_CHATROOMS)
#   print TEST_CHATROOMS['991'].getTopWords()
#   compare_concept=Concept()
#   compare_concept.importFromText("this weather sucks - it is far too rainy! I would far prefer if it was sunny.")
#   #compare_concept.top5chatrooms(TEST_CHATROOMS)
#   uid = createNewChatroom(compare_concept, TEST_CHATROOMS)
#   TEST_CHATROOMS[uid].getTopWords()

TEST_CHATROOMS['991'].add_user('adrian', '1')
TEST_CHATROOMS['991'].add_user('bartek', '2')
TEST_CHATROOMS['991'].add_user('daniel', '3')
TEST_CHATROOMS['991'].add_entry('1', "hello")
TEST_CHATROOMS['991'].add_entry('2', "hi")

print TEST_CHATROOMS['991'].entries



  
  
  
  


