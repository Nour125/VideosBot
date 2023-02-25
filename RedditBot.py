import datetime
import pyttsx3
import gtts
from playsound import playsound
import praw
from praw.models import MoreComments
engine = pyttsx3.init()
date = datetime.datetime.now()
mp3 = ".mp3"
zus = date.strftime("%d.%m.%Y") + mp3
commentsList = []

reddit = praw.Reddit(
    password="123poi??",
    username="ReadB629",
    client_id="V90ZcAcJHvtdIDcPnJZhrQ",
    client_secret="OH-XMcqE8mg0gwTDyOE4zFWk9ZMIDg",
    user_agent="ReadBot:1.0",
)


subReddit = reddit.subreddit("askReddit")
def hotsub():
    reddit.read_only = True
    for submission in subReddit.hot(limit = 1):
        cursub = submission
        sub = submission.title

    submission.comment_sort = "Top"
    submission.comments.replace_more(limit=1)
    for comment in cursub.comments:
        if isinstance(comment, MoreComments):
            continue
        com = comment.body
        #print(comment.body)
    reddit.read_only = False
    return (sub +"  "+ com)


def topsub():
    reddit.read_only = True
    for submission in subReddit.top(limit = 1):
        cursub = submission
        sub = submission.title

    submission.comments.replace_more(limit = 0)
    #submission.comment_sort = "new"
    commentsList = list(submission.comments) 
    topcom = commentsList[0]
    com = topcom.body
    reddit.read_only = False
    
    return (sub +" "+ com)


def tts (text):
    x = gtts.gTTS(text)
    x.save(zus)
   
y = topsub()
print(y)
print("done")