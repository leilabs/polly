import time
import tweepy
import requests

class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.auth = tweepy.OAuthHandler('v8xVBZlXBp2AJoWI3VjDjzDkC', 'Wpoom4N6tpTgfywzCt6y83gvZubbYoT0vL0V8FXzhyXA74218D')
        self.auth.set_access_token('734122414158708736-WijNUSxfi85hhqLGnaU8muQqInVugnE', 'PzXToKFTW0qErhvM4WIKerputvx5e0J1EM9aaObn5xNPJ')
        self.api = tweepy.API(self.auth)

    def on_direct_message(self, dm):
        message = dm._json['direct_message']['text']

        input_array = message.split("\n")

        number = input_array[0]
        text = input_array[1]

        data = { 'number': number, 'message': text }
        r = requests.post('http://textbelt.com/text', data=data)

        print dm._json['direct_message']['text']
        print r.text


MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=MyStreamListener.api.auth, listener=MyStreamListener)

myStream.userstream()