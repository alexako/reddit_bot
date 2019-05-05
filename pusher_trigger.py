from pusher import Pusher
import config

class Trigger():
    def __init__(self, bot, event, query, message):
        self.bot = bot
        self.event = event
        self.query = query
        self.message = message
        self.pusher = Pusher(
                app_id=config.APP_ID,
                key=config.KEY,
                secret=config.SECRET)

    def push(self):
        self.pusher.trigger(
                self.bot,
                self.event,
                {
                    u'query' : self.query,
                    u'message' : self.message
                }
            )

if __name__ == '__main__':
    trigger = Trigger("my-channel", "my-event", "query", "Hello world")
    trigger.push()