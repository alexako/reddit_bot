import redditBot
import datetime
import sys
from pusher_trigger import Trigger
from time import sleep


subreddit = "all"
limit = 1

def isInt(arg): #Check if int
    try:
        int(arg)
        return True
    except ValueError:
        return False

if len(sys.argv) > 1:
    query = " " + " ".join(sys.argv[1:]) + " "
else:
    print("Usage: python summon_bot.py [query]")
    sys.exit()

bot = redditBot.RedditBot(
        "SummonBot",
        "0.1",
        "/u/kludgebot"
        )

start_time = current_time = "".join(str(datetime.datetime.now()).split()[1].split(':')[:2])

print("Started on %s..." % (str(datetime.datetime.now()).split('.')[0]))
while True:
    message = "Hello"

    #Check comments
    # submission = bot.get_submissions(subreddit, limit)
    # comments = bot.get_comments(submission[0], query)
    # print("Results found: %d" % len(comments))

    # authors = ", ".join([str(comment.author) for comment in comments])
    # if len(authors) == 0:
        # trig_message = "No one has mentioned the trigger..."
        # comment_header = ''

    comments = bot.get_subreddit(subreddit).stream.comments()

    for comment in comments:

        if query in comment.body:
            #Build message
            trig_message = comment.author.name + " has mentioned the trigger!<br>"
            trig_message += comment.body
            comment_header = "Matching Comments:"
            message = """<p id="trigger_alert">
                <div id="query">Searched for: '%s'
                <br>
                Subreddit: /r/%s
                </div>
                <br>
                %s 
                </p>
                <p>
                <div id="post_title">%s</div> <br>
                <a id="post_link" href='%s'>%s</a> <br>
                <div id="date_performed">Last checked: %s</div>
                """ % (
                    query,
                    subreddit,
                    trig_message,
                    comment.submission.title,
                    comment.submission.shortlink,
                    comment.submission.shortlink,
                    str(datetime.datetime.now()).split('.')[0]
                )


            #Trigger
            trigger = Trigger(
                    "SummonBot", 
                    "summoned",
                    query,
                    message
                    )
            trigger.push()
            print("Notification pushed %s" % (str(datetime.datetime.now()).split('.')[0]))

    print("Sleeping...")
    #Sleep for 5 minutes
    sleep(5*60)

    #Update time
    current_time = "".join(str(datetime.datetime.now()).split()[1].split(':')[:2])

    print("Running on %s..." % (str(datetime.datetime.now()).split('.')[0]))
