import datetime
import pyttsx3
import random
import gtts
from playsound import playsound
from gtts.tokenizer import pre_processors
import moviepy.editor as video_editor
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
        #git Submissios
        for submission in subReddit.hot(limit = 100):
            submissionList.append(submission) 
        
        x = random.randrange(100)
        sub = submissionList[x].title
        cursub = submissionList[x]
        #git Comment
        cursub.comments.replace_more(limit = 0)
        #submission.comment_sort = "new"  #Macht iwie nichts    
        commentsList = list(cursub.comments) 
        i = 0
        topcom = commentsList[0]
        com = topcom.body
        commentwords = com.split(" ")
        #was wenn nichts gefunden wurde
        while((len(commentwords) < 75) & ((i+1) != len(commentsList))):
            topcom = commentsList[i]
            i += 1
            com = topcom.body
            commentwords = com.split(" ")
        if ((i+1) == len(commentsList)):
            subfound = False
        else:
            subfound = True
    
    reddit.read_only = False
    return (sub +"\n"+ com)


def pre_processing(text):
    pre_processors.tone_marks(text)
    pre_processors.end_of_line(text)
    pre_processors.abbreviations(text)
    pre_processors.word_sub(text)

def tts (text):
    x = gtts.gTTS(text, lang ='en', tld ='us')
    x.save(zus)
   

def create_video(video, subaudio):
    audio = video_editor.AudioFileClip(subaudio)
    clip = video_editor.VideoFileClip(video).subclip(audio.duration)
    clip = clip.volumex(0.8)



y = hotsub()
pre_processing(y)
tts(y)
print("done")