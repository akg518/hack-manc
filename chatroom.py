import random
import json

CHATROOMS = {}  #{uid:Chatroom}
CHATROOM_DATA = ["it is pretty rainy today, I don't want to go outside",
                 "I wander what to eat for lunch - maybe some stir fry?",
                 "I want new cook up some new recipes."
                 "it's a really nice weather today - I should go outside and play in the park!"
                 "camembert cheese is the best cheese"
                 "I'm tired, I need to get some fresh air"
                 "It's really cold outside, I should buy a new jacket"
                 "what is the best type of coffee?"
                 "that chocolate from coop is really good!"
                 "which country has the best weather?"
                 "I need more caffeine - I'm so tired!"
                 "Today's tuna sandwitches were really nice!"
                ]

class Chatroom():
    def __init__(self, *args, **kwargs):
      """
      two modes: either Chatroom(uid, concept)
      or Chatroom(JSONString = "JSON")
      """
        if "JSONString" in kwargs:
          self.__dict__ = json.loads(kwargs[JSONString])
        else:
          self.uid = args[0]
          self.concept = concept
          self.users = {}
          self.entries = [] # [(user, text)]        

    def getText():
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

    def __str__(self):
        key1 = self.concept.keywords
        key2 = sorted(key1.items(), key=lambda x: x[1])
        important = key2[-1][0] + " " + key2[-2][0] + " " + key2[-3][0]
        return str(important)

    def get_uid(self):
        return self.uid
      
    def toJSON(self):
      return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    @staticmethod
    def fromJSON(JSONString):
      

def createNewChatroom(self, concept):
    uid = ""
    while True:
        uid =str(random.randint(0, 100000))
        if uid not in CHATROOMS.keys():
            new_chatroom = Chatroom(uid, concept)
            global CHATROOMS
            CHATROOMS.append(new_chatroom)
            break
    return uid

def createTempChatrooms(chatroom_data):
  for input_string in chatroom_data:
    new_concept = Concept()
    
def saveCurrentChatrooms(filename):
  global CHATROOMS
  f = open(filename, 'w')
  f.write(json.dumps(CHATROOMS, sort_keys=True))
  f.close()
  
def loadChatrooms(filename):
  global CHATROOMS
  f = open(filename, 'r')
  CHATROOMS = json.loads(f.read())
  f.close()
  

        


