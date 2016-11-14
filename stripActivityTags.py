#Fetch activities and clean HTML tags

import httplib2
import json
import apiclient.discovery
from bs4 import BeautifulSoup
import nltk


#clean and strip html tags
def cleanHTML(html):
      if html =='':
            return ''

      soup = BeautifulSoup(html , "html.parser")
      return soup.get_text()

user_ID = '107033731246200681024'
API_KEY = 'AIzaSyDJYGj2_Wtq6QLE2B5G7KU4jz2w9A-uvwI'

service = apiclient.discovery.build('plus' , 'v1' ,
                                    http = httplib2.Http() ,
                                    developerKey = API_KEY)

activityFeed = service.activities().list(
      userId = user_ID,
      collection = 'public',
      maxResults = 100).execute()

print(cleanHTML(activityFeed['items'][0]['object']['content']))
