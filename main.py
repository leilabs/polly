import tweepy, requests, time
from cowpy import cow

cheese = cow.Milk()

class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.auth = tweepy.OAuthHandler('v8xVBZlXBp2AJoWI3VjDjzDkC', 'Wpoom4N6tpTgfywzCt6y83gvZubbYoT0vL0V8FXzhyXA74218D')
        self.auth.set_access_token('734122414158708736-WijNUSxfi85hhqLGnaU8muQqInVugnE', 'PzXToKFTW0qErhvM4WIKerputvx5e0J1EM9aaObn5xNPJ')
        self.api = tweepy.API(self.auth)

        self.example = u'Polly Help:\n\n4253221077\nThe government is watching us at every moment\n[Canada/Intl]'

    def on_direct_message(self, dm):
        self.message = dm._json['direct_message']

        text = unicode(self.message[u'text'])
        inputs = text.split('\n')
        user = unicode(self.message['sender']['screen_name'])

        if user != u'MessagePolly':
            if len(inputs) < 2:
                # givem some help
                self.dm(user, self.example)
                self.log(u'Sending help to {}'.format(user))
            else:
                data = { 'number': inputs[0], 'message': inputs[1], 'from': user}
                self.log(u'Sending "{message}" to {number} from @{from}'.format(**data))

                # check if intl, us, or canada
                if len(inputs) == 2:
                    r = requests.post('http://textbelt.com/text', data=data)
                elif inputs[2] is not None:
                    if inputs[2].lower() == 'canada':
                        r = requests.post('http://textbelt.com/canada', data=data)
                    elif inputs[2].lower() == 'intl':
                        r = requests.post('http://textbelt.com/intl', data=data)
                    else:
                        self.log(u'Error: Unrecognized area: {}'.format(inputs[2]))
                        self.dm(user, u'Error: Unrecognized area: {}'.format(inputs[2]))

                # check success and throw error if things didn't work out too well
                try:
                    if r.json()['success']:
                        res = u'Your message ({message}) to {number} has been sent succesfully.'.format(**data)
                        self.log(res)
                        self.dm(user, res)
                    else:
                        error = u'Your text didn\'t send. {}'.format(r.json()['message'])
                        self.log(error)
                        self.dm(user, error)
                except:
                    pass

    def dm(self, user, dm):
        try:
            self.api.send_direct_message(user=user, text=dm)
        except:
            self.log(u'Error: Tried to send "{}..." to {}'.format(dm[0:8], user))

    def log(self, m):
        text = u"=> " + time.strftime("%Y-%m-%d %H:%M:%S") + u' {}'.format(m)

        file = open('log_' + time.strftime("%m-%d-%Y")+'.log', mode='w')
        file.write(text.encode('utf8'))
        file.close()

        print text

MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=MyStreamListener.api.auth, listener=MyStreamListener)

print cheese.milk('Running @MessagePolly...')
myStream.userstream()