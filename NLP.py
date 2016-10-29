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

    if response['status'] == 'OK':
        for keyword in response['keywords']:
            print('text: ', keyword['text'].encode('utf-8'))
            print('relevance: ', keyword['relevance'])
            print('sentiment: ', keyword['sentiment']['type'])

    else:
        print('Error in keyword extaction call: ', response['statusInfo'])

    return response


def getTaxonomy(string):

    inputText = string
    response = alchemyapi.taxonomy('text', inputText)

    if response['status'] == 'OK':

        for category in response['taxonomy']:
            print(category['label'], ' : ', category['score'])
        print('')

    else:
        print('Error in taxonomy call: ', response['statusInfo'])

    return response