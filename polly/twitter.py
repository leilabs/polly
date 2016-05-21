import tweepy

class Twitter():
	def __init__(self):
		auth = tweepy.OAuthHandler('P9cfEjjxkNMZ6O7R77ZNgLA7y', 'ogdH9lSibMMNefxCckcbUY5mcmJETcrfwTecdZ6UQjvjMYuUHr')
		auth.set_access_token('734122414158708736-aIU91UlFlTYLNz6vwwkaGASzkZefq7K', 'SrhfOtahRiANZ0HTb3LTqDO6LWOGovUacNVWpyZ09DZna')
		self.api = tweepy.API(auth)

		# follow users back
		for follower in tweepy.Cursor(self.api.followers).items():
			follower.follow()

	def dms(self):
		return self.api.direct_messages()