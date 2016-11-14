#get comments from Google+ Users


import os
import httplib2
import json
import apiclient.discovery
from bs4 import BeautifulSoup
import nltk


API_KEY = 'AIzaSyDJYGj2_Wtq6QLE2B5G7KU4jz2w9A-uvwI'

activity_id = "z12zzdcixrevff3e323ns1fjbtiwwpw2u"

service = apiclient.discovery.build('plus' , 'v1' ,
                                    http = httplib2.Http(),
                                    developerKey = API_KEY)



comments_resource = service.comments()
comments_document = comments_resource.list( \
    maxResults=10,activityId=activity_id).execute()

if 'items' in comments_document:
  print('got page with %d' % len( comments_document['items'] ))
  for comment in comments_document['items']:
    print(comment['id'], comment['object']['content'])
