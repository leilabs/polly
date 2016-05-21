import requests

class Text():
	def __init__(self):
		pass

	def send(self, to, body):
		data = { 'number': self.to, 'message': self.body }
		r = requests.post('http://textbelt.com/text', data=data)