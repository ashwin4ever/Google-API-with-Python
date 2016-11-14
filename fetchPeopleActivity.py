#Fetching recent activities using Google+ API

import httplib2
import json
import apiclient.discovery

user_ID = '107033731246200681024'

API_KEY = 'AIzaSyDJYGj2_Wtq6QLE2B5G7KU4jz2w9A-uvwI'
service = apiclient.discovery.build('plus' , 'v1' ,
                                    http = httplib2.Http(),
                                    developerKey = API_KEY)

activityFeed = service.activities().list(
      userId = user_ID,
      collection = 'public',
      maxResults = '1' # max allowed
      ).execute()

print(json.dumps(activityFeed['items'][0]['object']['content'] , indent = 2))
      
