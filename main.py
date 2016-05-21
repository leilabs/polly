from polly.textbelt import Text
from polly.twitter import Twitter
import time

t = Twitter()
# t.send('9713036121', 'this is a test')

for dm in t.dms():
	print dm.text