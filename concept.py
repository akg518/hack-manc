import json

from NLP import getTaxonomy, getKeywords


class Concept:
  keyword_weight = 0.4
  topic_weight = 0.4
  sentiment_weight = 0.2  

  def __init__(self):
    self.keywords = {}
    self.topics = {} #TOPICS = TAXONOMY!!!!
    self.sentiment = 0 # value between -1 and 1


  def importFromText(self, input_string):
    """
    fills out all the concept attributes#
    and topics as expected.
    """
    
    keywordJSON = getKeywords(input_string)
    taxonomyJSON = getTaxonomy(input_string)
    
    self.sentiment = 0
    keyword_num = len(keywordJSON)
    
    for keyword in keywordJSON['keywords']:
      self.keywords[keyword['text']] = float(keyword['relevance'])
      sentiment = keyword['sentiment']['type'].encode('utf-8')
      if sentiment == 'positive':
        self.sentiment += float(keyword['relevance'])
      else:
        self.sentiment -= float(keyword['relevance'])
    
    self.sentiment /= keyword_num
    
    for category in taxonomyJSON['taxonomy']:
      self.topics[category['label']] = float(category['score'])

#     for x in self.keywords:
#       print str(x) + ":" + str(self.keywords[x])

#     for x in self.topics:
#       str(x) + ":" + str(self.topics[x])

  def compare (self, other):
    """
    compares two concepts and returns a relevance score between 0 and 1
    """
    similarity_ranking = 0
    for keyword in self.keywords:
      if keyword in other.keywords:
        score_addon = self.keywords[keyword] * other.keywords[keyword] * Concept.keyword_weight
        print "addon " + str(score_addon) + " for keyword " + keyword
        similarity_ranking += score_addon
        
    for topic in self.topics:
      if topic in other.topics:
        score_addon = self.topics[topic] * other.topics[topic] * Concept.topic_weight
        print "addon " + str(score_addon) + " for topic " + topic
        similarity_ranking += score_addon
        
    score_addon = self.sentiment*other.sentiment * Concept.sentiment_weight
    print "addon " + str(score_addon) + " for overall sentiment"
    similarity_ranking += score_addon
      
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
  
  def __str__(self):
    result = ""
    result += "keywords: " + str(self.keywords) + '\n'
    result += "topics: " + str(self.topics) + '\n'
    result += "sentiment: " + str(self.sentiment)
    return result
    
if __name__=="__main__":
  c = Concept()
  d = Concept()
  d.importFromText("its pretty cloudy today, I'm hoping for the some sun!")
  c.importFromText("Today is a really good weather. I like how sunny it is!")

  print "C DATA"
  print c
  print "D DATA"
  print d
  print "COMPARISON"
  print "relevance" + str(c.compare(d))

