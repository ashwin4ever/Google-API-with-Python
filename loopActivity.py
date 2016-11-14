#looping over multiple pages of Google+ activities

import os
import httplib2
import json
import apiclient.discovery
from bs4 import BeautifulSoup
import nltk

user_ID = '105045141516775240108'
API_KEY = 'AIzaSyDJYGj2_Wtq6QLE2B5G7KU4jz2w9A-uvwI'


MAX_RESULTS = 50

def cleanHTML(html):
      if html == "":
            return ""

      soup = BeautifulSoup(html , "html.parser")
      #soup = soup.encode("utf-8")

      return soup.get_text()

service = apiclient.discovery.build('plus' , 'v1' ,
                                    http = httplib2.Http(),
                                    developerKey = API_KEY)

# define the activities for the user
activity_feed = service.activities().list(
      userId = user_ID,
      collection = 'public',
      maxResults = '100')

activity_results = []
activity_id = []
print(activity_feed)




while activity_feed != None and len(activity_results) < MAX_RESULTS:

      activities = activity_feed.execute()

      if 'items' in activities:
            for act in activities['items']:
                  print('activity item: ' , act)
                  activity_id.append(act['id'])
                  #if act['object']['objectType'] == 'note' and \
                  if act['object']['content'] != '':

                        act['title'] = cleanHTML(act['title'])
                        act['object']['content'] = cleanHTML(act['object']['content'])
                        activity_results += [act['object']['content']]

            activity_feed = service.activities().list_next(activity_feed , activities)


#print(str(activity_results))
#write the output to a file
f = open(os.path.join('C:\\Users\\Ashwin\\Desktop\\game making\\Google API\\' , user_ID + '.txt' ) , 'w' , encoding = 'cp1252' , errors = 'replace')
#f.write(json.dumps(activity_results , indent = 2))
f.write(str(activity_results))
f.close()

print("\n")

tokens = [nltk.word_tokenize(w) for w in activity_results]
#print(tokens)

print(activity_id)
print(str(len(activity_results)) , " activities written to : " , f.name)


