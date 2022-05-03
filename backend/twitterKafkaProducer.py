from json import dumps
import tweepy
from tweepy import OAuthHandler
from kafka import KafkaProducer
from datetime import datetime

def kafkaProducer(keyword):
# arguments
    print("keyword" + keyword)
        
    presentTime = datetime.now()

    current_time = presentTime.strftime("%H:%M:%S")
    
    topic_name = 'kafkatwitter_1'

# get keywords
    keywords_to_track = [keyword]

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

# init kafka producer
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'),
                         api_version=(0, 10, 1))

# Step 1: Creating a StreamListener: override tweepy.StreamListener to add logic to on_status
    class MyStreamListener(tweepy.Stream):
        def on_status(self, tweet):
            length = len(tweet.text.split(' '))
            if (tweet.lang != 'en') or (length <= 10):
                pass
                print("==filtered==")
            else:
                message = { "text": tweet.text }

                print("message:", message)
                producer.send(topic_name, value=message)

        def on_error(self, status_code):
            print(status_code)

            if status_code == 420:
                # returning False in on_error disconnects the stream
                return False

    myStream = MyStreamListener(API_KEY, API_KEY_SECRET,ACCESS_TOKEN, ACCESS_SECRET)

# Step 3: Starting a Stream
    myStream.filter(track=keywords_to_track)

    return "success"
