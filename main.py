from polly.textbelt import Text
from polly.twitter import Twitter
import time

t = Twitter()
# t.send('9713036121', 'this is a test')

length = len(t.dms())

while (True):
	if len(t.dms()) > length:
		length = len(t.dms())
		print 'new dm (used to have {}, now has {})'.format(length, len(t.dms()))
	time.sleep(2)