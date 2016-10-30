"""
Natural Language Processing
***************************

Takes string as an argument
returns keywords and taxonomy

"""


from alchemyapi import AlchemyAPI
import json, getopt, sys
alchemyapi = AlchemyAPI()




def getKeywords(string):
    inputText = string
    response = alchemyapi.keywords('text', inputText, {'sentiment': 1})
    return response


def getTaxonomy(string):

    inputText = string
    response = alchemyapi.taxonomy('text', inputText)

    return response
  
