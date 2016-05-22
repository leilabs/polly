import time
import tweepy
import requests

class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.auth = tweepy.OAuthHandler('v8xVBZlXBp2AJoWI3VjDjzDkC', 'Wpoom4N6tpTgfywzCt6y83gvZubbYoT0vL0V8FXzhyXA74218D')
        self.auth.set_access_token('734122414158708736-WijNUSxfi85hhqLGnaU8muQqInVugnE', 'PzXToKFTW0qErhvM4WIKerputvx5e0J1EM9aaObn5xNPJ')
        self.api = tweepy.API(self.auth)

    def on_direct_message(self, dm):
        message = dm._json['direct_message']
        text = message['text']

        input_array = text.split('\n')

        number, body = input_array[0], input_array[1]

        data = { 'number': number, 'message': body }
        r = requests.post('http://textbelt.com/text', data=data)

        if r.json()['success']:
        	self.log('Sent "{message}" to {number}'.format(**data))
        else:
        	self.log('Failed with Error: {}'.format(r.json()['message']))

    def log(self, m):
    	print "=> %s" % m


MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=MyStreamListener.api.auth, listener=MyStreamListener)

myStream.userstream()