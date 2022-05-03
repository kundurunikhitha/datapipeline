import errno
import flask
from pytz import country_names
import twitterCountryHashtags
from flask import request
import sys
import twitterKafkaProducer as kp
import test

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

global time
global country
global hashtag
global name

@app.route('/getAll', methods=['GET'])
def getCountries():
    return  str(twitterCountryHashtags.get_countries());

@app.route('/country', methods=['GET'])
def getTrendingHashtags():
    countryid = request.args.get('country')
    return  str(twitterCountryHashtags.get_hashtags(countryid));

@app.route('/getValues', methods=['POST'])
def postvalues():
    getJson = request.get_json()
    time = getJson['time']
    regionName = getJson['regionName']
    regionType = getJson['regionType']
    hashtag = getJson['hashtag']
    name = getJson['name']
    print(getJson['name'])
    print(getJson['regionType'])
    print(getJson['hashtag'])
    print(getJson['time'])
    print(getJson['regionName'])
    '''try:
        test.testFun();
    except:
        print(errno);
    return "request";'''

app.run()