#exploring nltk using google+ data

import nltk
import os
import httplib2
import json
import apiclient.discovery
from bs4 import BeautifulSoup

USER_ID = '107033731246200681024'
API_KEY = 'AIzaSyDJYGj2_Wtq6QLE2B5G7KU4jz2w9A-uvwI'

MAX_RESULTS = 100


def cleanHTML(html):
      if html == "":
            return ""

      soup = BeautifulSoup(html , "html.parser")

      return soup.get_text()

#define a service for Google+
service = apiclient.discovery.build('plus' , 'v1' ,
                                    http = httplib2.Http() ,
                                    developerKey = API_KEY)

#define activities for the user
#and execute it to get the data
activity_feed = service.activities().list(
      userId = USER_ID,
      collection = 'public',
      maxResults = '100')

activity_results = []

while activity_feed != None and len(activity_results) < MAX_RESULTS:

      activities = activity_feed.execute()

      if 'items' in activities:
            for act in activities['items']:

                  if act['object']['objectType'] == 'note' and \
                     act['object']['content'] != '':

                        act['title'] = cleanHTML(act['title'])
                        act['object']['content'] = cleanHTML(act['object']['content'])
                        activity_results += [act]

            activity_feed = service.activities().list_next(activity_feed , activities)
            
                        
#write output to a json file
f = open(os.path.join('C:\\Users\\Ashwin\\Desktop\\game making\\Google API\\' , 'nltkTest.json') , 'w' , encoding = 'cp1252' , errors = 'replace')
f.write(json.dumps(activity_results , indent = 2))
f.close()
print(str(len(activity_results)) , " activities written to : " , f.name)


allContent = " ".join(a['object']['content'] for a in activity_results)

print("Length of all contents: " ,len(allContent))

tokens = allContent.split()
text = nltk.Text(tokens)


text.concordance('open')
print('\n')
text.collocations()
