"""
Natural Language Processing
***************************

Takes string as an argument
returns keywords and taxonomy

"""


from alchemyapi import AlchemyAPI
import json

alchemyapi = AlchemyAPI()



def getStringInfo(string):



    inputText = string


    print('#   input:                                 #')

    print inputText


    print('#   Keywords + sentiment                   #')


    response = alchemyapi.sentiment("text", inputText)
    print "Sentiment: ", response["docSentiment"]["type"]




    response = alchemyapi.keywords('text', inputText, {'sentiment': 1})

    if response['status'] == 'OK':
        print('## Response Object ##')
        print(json.dumps(response, indent=4))

        print('')
        print('## Keywords ##')
        for keyword in response['keywords']:
            print('text: ', keyword['text'].encode('utf-8'))
            print('relevance: ', keyword['relevance'])
            print('sentiment: ', keyword['sentiment']['type'])
            if 'score' in keyword['sentiment']:
                print('sentiment score: ' + keyword['sentiment']['score'])
            print('')
    else:
        print('Error in keyword extaction call: ', response['statusInfo'])


    print('#   Taxonomy                       #')


    print('Processing text: ', inputText)
    print('')

    response = alchemyapi.taxonomy('text', inputText)

    if response['status'] == 'OK':
        print('## Response Object ##')
        print(json.dumps(response, indent=4))

        print('')
        print('## Categories ##')
        for category in response['taxonomy']:
            print(category['label'], ' : ', category['score'])
        print('')

    else:
        print('Error in taxonomy call: ', response['statusInfo'])

    print('')
    print('')



    return "abc"