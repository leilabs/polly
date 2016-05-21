import tweepy

class Twitter():
	def __init__(self):
		auth = tweepy.OAuthHandler('v8xVBZlXBp2AJoWI3VjDjzDkC', 'Wpoom4N6tpTgfywzCt6y83gvZubbYoT0vL0V8FXzhyXA74218D')
		auth.set_access_token('734122414158708736-WijNUSxfi85hhqLGnaU8muQqInVugnE', 'PzXToKFTW0qErhvM4WIKerputvx5e0J1EM9aaObn5xNPJ')
		self.api = tweepy.API(auth)

		# follow users back
		for follower in tweepy.Cursor(self.api.followers).items():
			follower.follow()

	def dms(self):
		return self.api.direct_messages()

class MyStreamListener(tweepy.StreamListener):
	def __init__(self):
		pass

	def on_dm(self, dm):
		print(dm.text)

	def on_status(self, status):
		print(status.text)

auth = tweepy.OAuthHandler('v8xVBZlXBp2AJoWI3VjDjzDkC', 'Wpoom4N6tpTgfywzCt6y83gvZubbYoT0vL0V8FXzhyXA74218D')
auth.set_access_token('734122414158708736-WijNUSxfi85hhqLGnaU8muQqInVugnE', 'PzXToKFTW0qErhvM4WIKerputvx5e0J1EM9aaObn5xNPJ')
api = tweepy.API(auth)

MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener)

print hasattr(myStream,"method")
dir(myStream)