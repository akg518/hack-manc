import json

from NLP import getTaxonomy, getKeywords


class concept:


  def __init__(self, score=None):
    self.keywords = {}
    self.topics = {} #TOPICS = TAXONOMY!!!!
    self.sentiment = {self.sentiment: "none", score : 0}
  def importFromJSON(JSON):
    """
    takes a JSON file as a string and fills out all the concept attributes#
    and topics as expected.
    """
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

  def top10chatrooms(self, chatroomList):
    """
    takes the chatrooms list and returns top 10 most relevant chatrooms
    """
    top10 = []
    scorings = {}
    for chatroom in chatroomList:
      scorings[chatroom.id] = self.compare(chatroom.concept)
    #przesortowac
    #top 10 do top10


  getTaxonomy("good day bad weather bank list well done")
  getKeywords("good day bad weather bank list well done")