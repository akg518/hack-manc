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
            print('sentiment: ', keyword['sentiment']['type'].encode('utf-8'))

    else:
        print('Error in keyword extaction call: ', response['statusInfo'])

    return response


def getTaxonomy(string):

    inputText = string
    response = alchemyapi.taxonomy('text', inputText)

    if not response['status'] == 'OK':

        print('Error in taxonomy call: ', response['statusInfo'])

    return response