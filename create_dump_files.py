import chatroom_store, concept, chatroom


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
                 "Today's tuna sandwiches were really nice!",
                 "Does anyone know where I can get fresh cucumber",
                 "I hate when my jeans are too tight",
                 "I have found a fantastic pizza place in my neighbourhood",
                 "It's important to wear matching pairs of clothing",
                 "How can people add pickles to salads?!",
                 "I'm trying to save up for the new pair of shoes",
                 "do you think it always rains in scotland?",
                 "I'm looking for a substitute for bread, I really need to go on diet"]

CHATROOMS = chatroom_store.ChatroomStore()

if __name__ == "__main__":
    for sentence in CHATROOM_DATA:
        new_concept = concept.Concept()
        new_concept.importFromText(sentence)
        new_chatroom = chatroom.Chatroom(new_concept)
        CHATROOMS.add_chatroom(new_chatroom)
    CHATROOMS.save_chatrooms_to_JSON("dumps.json")
