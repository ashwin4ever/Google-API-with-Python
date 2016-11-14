#Searching for a person using Google+ API

import httplib2
import json
import apiclient.discovery


#enter any persons name
personName = "Tim O'Reilly"

API_KEY = 'AIzaSyDJYGj2_Wtq6QLE2B5G7KU4jz2w9A-uvwI'

service = apiclient.discovery.build('plus' , 'v1' ,
                                    http = httplib2.Http(),
                                    developerKey = API_KEY)

peopleFeed = service.people().search(query = personName).execute()

print(json.dumps(peopleFeed, indent = 2))
