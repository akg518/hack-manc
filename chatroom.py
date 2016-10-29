import random
CHATROOMS = {}  #{uid:Chatroom}

class Chatroom():
    def __init__(self, uid, concept):
        self.uid = uid
        self.concept = concept
        self.users = []
        self.entries = [] # [(user, text)]

    def getText():
        return '\n'.join([': '.join(row) for row in self.entries])

    def add_user(self, user):
        self.users.append(user)

    def add_entry(self, user, text):
        self.entries.append((user, text))
        if len(self.entries) > 20:
            self.entries = self.entries[-20:]

    def __str__(self):
        key1 = self.concept.keywords
        key2 = sorted(key1.items(), key=lambda x: x[1])
        important = key2[-1][0] + " " + key2[-2][0] + " " + key2[-3][0]
        return str(important)

    def __repr__(self):
        return self.uid

    def createNewChatroom(self, concept):
        while True:
            uid =str(random.randint(0, 100000))
            if uid not in CHATROOMS.keys():
                new_chatroom = Chatroom(uid, concept)
                global CHATROOMS
                CHATROOMS.append(new_chatroom)
                break


