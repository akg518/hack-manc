import json

from NLP import getTaxonomy, getKeywords


class Concept:


  def __init__(self):
    self.input_string = "good day bad weather bank list well done"
    self.keywords = {}
    self.topics = {} #TOPICS = TAXONOMY!!!!
    self.sentiment = ["none", 0]


  def importFromJSON(self):
    """
    fills out all the concept attributes#
    and topics as expected.
    """
    keywordJSON = getKeywords(self.input_string)
    for keyword in keywordJSON['keywords']:
     self.keywords[keyword['text']] = keyword['relevance']

    taxonomyJSON = getTaxonomy(self.input_string)
    for category in taxonomyJSON['taxonomy']:
      self.topics[category['label']] = category['score']



    for x in self.keywords:
      print(x)
      print self.keywords[x]

    for x in self.topics:
      print(x)
      print self.topics[x]


    print "ok"

    #TODO finish me
    pass
  def compare (self, other):
    """
    compares two concepts and returns a relevance score between 0 and 1
    """
    similarity_ranking = 0
    for keyword in self.keywords:
      if keyword in other.keywords:
        similarity_ranking += self.keywords[keyword] * other.keywords[keyword] * Concept.keywords_weighting
        
    for topic in self.topics:
      if topic in other.topics:
        similarity_ranking += self.topics[topic] * other.topics[topic] * Concept.topic_weighting
        
    if self.sentiment["sentiment_type"] == other.sentiment["sentiment_type"]:
      similarity_ranking += self.sentiment["value"]*other.sentiment["value"] * Concept.sentiment_weighting
      
    return similarity_ranking

  def top5chatrooms(self, chatroomList):
    """
    takes the chatrooms list and returns top 10 most relevant chatrooms
    """
    top5 = []
    scorings = {}
    for chatroom in chatroomList:
      scorings[chatroom.id] = self.compare(chatroom.concept)
    #przesortowac
    #top 10 do top10



c = Concept()
c.importFromJSON()
