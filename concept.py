class concept:
  def __init__(self):
    self.keywords = {}
    self.topics = {} #TOPICS = TAXONOMY!!!!
    self.sentiment = {sentiment : "none", score : 0}
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
    pass

  def top10chatrooms(self, chatroomList):
    """
    takes the chatrooms list and returns top 10 most relevant chatrooms
    """
    pass
    