import datetime
import pyttsx3
import gtts
import random
from playsound import playsound
import praw
from praw.models import MoreComments
engine = pyttsx3.init()
date = datetime.datetime.now()
mp3 = ".mp3"
zus = date.strftime("%d.%m.%Y") + mp3
commentsList = []
submissionList = []
commentwords = list()

lenOfCom = 0
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
    subfound = False
    while(subfound == False):

        for submission in subReddit.hot(limit = 100):
            submissionList.append(submission) 
        
        x = random.randrange(100)
        sub = submissionList[x].title
        cursub = submissionList[x]
        
        cursub.comments.replace_more(limit = 0)
        #submission.comment_sort = "new"  #Macht iwie nichts    
        commentsList = list(cursub.comments) 
        i = 0
        topcom = commentsList[0]
        com = topcom.body
        commentwords = com.split(" ")
        #firstlen = commentwords
        #was wenn nichts gefunden wurde
        while((len(commentwords) < 75) & ((i+1) != len(commentsList))):
            topcom = commentsList[i]
            print(len(commentsList))
            print(i)
            i += 1
            com = topcom.body
            commentwords = com.split(" ")
            #curlen = len(commentwords)

        if ((i+1) == len(commentsList)):
            subfound = False
        else:
            subfound = True
    
    reddit.read_only = False
    return (sub +"\n"+ com)


def topsub():
    reddit.read_only = True

    for submission in subReddit.top(limit = 100):
        submissionList.append(submission) 
    
    sub = submissionList[0].title
    cursub = submissionList[0]
    
    cursub.comments.replace_more(limit = 0)
    #submission.comment_sort = "new"      
    commentsList = list(cursub.comments) 
    i = 1
    topcom = commentsList[0]
    com = topcom.body
    commentwords = com.split(" ")
    while(len(commentwords) < 50):
        topcom = commentsList[i]
        i += 1
        com = topcom.body
        commentwords = com.split(" ")
    reddit.read_only = False

    return (sub +" "+ com)


def tts (text):
    x = gtts.gTTS(text)
    x.save(zus)
   
y = hotsub()
tts(y)
print("done")