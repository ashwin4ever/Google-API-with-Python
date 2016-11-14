#search for google profiles


import apiclient.discovery
import httplib2
import nltk


API_KEY = 'AIzaSyDJYGj2_Wtq6QLE2B5G7KU4jz2w9A-uvwI'
service = apiclient.discovery.build('plus' , 'v1' ,
                                    http = httplib2.Http(),
                                    developerKey = API_KEY)

peopleResource = service.people()
peopleDoc = peopleResource.search(maxResults = 35 ,
                                  query = 'President 2016').execute()

if 'items' in peopleDoc:
      print('Got page with %d' , len(peopleDoc['items']))

      for person in peopleDoc['items']:
            print("Person id: " , person['id'] , " Name: " , person['displayName'])

