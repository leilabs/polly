import requests

class Text():
	def __init__(self, to, body):
		self.to = to
		self.body = body

	def request(self):
		data = { 'number': self.to, 'message': self.body }
		r = requests.post('http://textbelt.com/text', data = data)