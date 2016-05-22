import time, tweepy, requests

class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.auth = tweepy.OAuthHandler('v8xVBZlXBp2AJoWI3VjDjzDkC', 'Wpoom4N6tpTgfywzCt6y83gvZubbYoT0vL0V8FXzhyXA74218D')
        self.auth.set_access_token('734122414158708736-WijNUSxfi85hhqLGnaU8muQqInVugnE', 'PzXToKFTW0qErhvM4WIKerputvx5e0J1EM9aaObn5xNPJ')
        self.api = tweepy.API(self.auth)

        self.example = 'Example:\n\n123456789\nHey dude'

    def dm(self, user, dm):
        time.sleep(1)
        try:
            self.api.send_direct_message(user=user, text=dm)
        except:
            self.log('Error: Tried to send "{}..." to {}'.format(dm[0:8], user))

    def on_direct_message(self, dm):
        self.message = dm._json['direct_message']

        text = self.message['text']
        inputs = text.split('\n')
        user = str(self.message['sender']['screen_name'])

        if user is not 'MessagePolly':
            if len(inputs) < 2:
                # givem some help
                self.dm(user, self.example)
            else:
                data = { 'number': inputs[0], 'message': inputs[1] }
                print 'sending "{message}" to {number}'.format(**data)
                r = requests.post('http://textbelt.com/text', data=data)

                # check success and throw error if things didn't work out too well
                if r.json()['success']:
                    res = 'Your message ({message}) to {number} has been sent succesfully.'.format(**data)
                    self.log(res)
                    self.dm(user, res)
                else:
                    error = 'Your text didn\'t send. {}'.format(r.json()['message'])
                    self.log(error)
                    self.dm(user, error)

    def log(self, m):
        logtext = "=> "+time.strftime("%Y-%m-%d %H:%M:%S")+" %s" % m

        file = open("log_"+time.strftime("%m-%d-%Y")+".log", "w")
        file.write(logtext)

        print logtext
        file.close()

MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=MyStreamListener.api.auth, listener=MyStreamListener)

print 'Running @MessagePolly...'
myStream.userstream()