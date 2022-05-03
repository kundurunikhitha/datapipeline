import tweepy
from tweepy import OAuthHandler
import json
global countryName
def extract_hashtags(woeid):
    trends = api.get_place_trends(woeid)
    hashtags = [trend["name"] for trend in trends[0]["trends"] if "#" in trend["name"]]
    return hashtags

# twitter keys
API_KEY = 'pvV0IpKzooJrSUQullBR0HiUr'
API_KEY_SECRET = 'bGzQBF8QtGhby6SAysXmowAAKxeLmwtn473AXS00ZY11X1wwPL'
ACCESS_TOKEN = '1486616689659817986-yUpoV9TPhYcfiiesbJoIGCvY98ma4c'
ACCESS_SECRET = '78LIwEDBMUYN6wLF4xOt0Pmdf4TEPjZ0TXTdzTDDQh5yI'

# twitter authorization
auth = OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# init tweepy
api = tweepy.API(auth)

available_loc = api.available_trends()
countryList = []
for i in range(0,len(available_loc)):
    countryList.append(available_loc[i]['name'])
    countryList.sort()

def get_countries():
    return json.dumps(available_loc)
def get_hashtags(data):
    return json.dumps(extract_hashtags(data))
 



