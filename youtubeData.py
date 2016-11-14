#Data Mining from Youtube

from apiclient.discovery import build_from_document
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
import pandas as pd
import json
import os
import sys
import httplib2


API_KEY = 'AIzaSyDJYGj2_Wtq6QLE2B5G7KU4jz2w9A-uvwI'

YOUTUBE_SERVICE_NAME = 'youtube'
YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtubepartner"
API_VER = 'v3'

argparser.add_argument("--q" , help = "Search Term" , default = "Creating subtitles and closed captions")
argparser.add_argument("--max-results" , help = "Max Results" , default = 1)
args = argparser.parse_args()
options = args
capID = []

CLIENT_SECRETS_FILE = "client_secrets.json"


MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:
   %s
with information from the APIs Console
https://console.developers.google.com

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))



def get_authenticated_service(args):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SSL_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("%s-oauth2.json" % sys.argv[0])
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage, args)

  # Trusted testers can download this discovery document from the developers page
  # and it should be in the same directory with the code.
  with open("youtube-v3-api-captions.json", "r") as f:
    doc = f.read()
    return build_from_document(doc, http=credentials.authorize(httplib2.Http()))


youtubeService = get_authenticated_service(options)

#youtubeService = build(YOUTUBE_SERVICE_NAME , API_VER , developerKey = API_KEY)


searchVids = youtubeService.search().list(
      q = options.q,
      type = "video",
      part = "id , snippet",
      maxResults = options.max_results).execute()

vidDict = {}

print(json.dumps(searchVids , indent = 4))

for vids in searchVids.get("items" , []):
      if vids["id"]["kind"] == "youtube#video":
            vidDict[vids["id"]["videoId"]] = vids["snippet"]["title"]


print(vidDict)
print("\n")
#List captions to get caption ID

def listCaptions(youtubeService , video_id):
      caps = youtubeService.captions().list(
            part = "id , snippet",
            videoId = video_id).execute()


      print("Captions")
      print("\n")
      print(json.dumps(caps , indent = 4))

      for item in caps["items"]:
            capID.append(item["id"])
            



#Loop over dict key (Videos) to get caption ID
for vidKey in vidDict:
      listCaptions(youtubeService , vidKey)

print("\ncaption ID is : " , capID)



#Download or print captions

def downloadCaptions(youtubeService , caption_id):
      subs = youtubeService.captions().download(
            id = caption_id
            
            ).execute()
      print("\n")
      print(json.dumps(subs , indent = 4))

for i in capID:
      downloadCaptions(youtubeService , i)



