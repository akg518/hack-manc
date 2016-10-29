import json

from NLP import getTaxonomy, getKeywords


class Concept:


  def __init__(self):
    self.keywords = {}
    self.topics = {} #TOPICS = TAXONOMY!!!!
    self.sentiment = ["none", 0]


  def importFromJSON(self, input_string):
    """
    fills out all the concept attributes#
    and topics as expected.
    """
    
    positivity_score = 0
    keyword_num = 0
    
    keywordJSON = getKeywords(input_string)
    
    
    for keyword in keywordJSON['keywords']:
      self.keywords[keyword['text']] = keyword['relevance']
      sentiment = keyword['sentiment']['type'].encode('utf-8')
      if sentiment == 'positive':
        positivity_score += relevance
      else:
        positivity_score -= relevance
        
    pos

    taxonomyJSON = getTaxonomy(input_string)
    for category in taxonomyJSON['taxonomy']:
      self.topics[category['label']] = category['score']



    for x in self.keywords:
      print str(x) + ":" + str(self.keywords[x])

    for x in self.topics:
      str(x) + ":" + str(self.topics[x])

      
    for 
  

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
    
    dic2 = sorted(scorings.items(), key=lambda x: x[1])
    top5 = dic2[-5:]
    return top5



c = Concept()
c.importFromJSON()
