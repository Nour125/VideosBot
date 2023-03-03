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
   

def cut_one_min(video):
    start = random.randrange(1, 180)
    ende  = start + 6 #Bestimmt wie viel Sekunden ausm video genommen werden
    print(start)
    print(ende)
    cur = video_editor.VideoFileClip(video).subclip(start * 10, ende * 10)
    return cur


def add_ten_sekunden(video):
    start = random.randrange(1, 180)
    ende  = start + 1 #Bestimmt wie viel Sekunden ausm video genommen werden
    ten_sec_clip = video_editor.VideoFileClip(video).subclip(start * 10, ende * 10)
    final_clip = video_editor.concatenate_videoclips([video,ten_sec_clip])
    return final_clip

def create_video(video, subaudio):
    audio = video_editor.AudioFileClip(subaudio)
    clip = video_editor.VideoFileClip(video)
    while(clip.duration < audio.duration):
        clip = add_ten_sekunden(clip)
    clip = video_editor.VideoFileClip.subclip(0,audio.duration)
    clip = clip.volumex(0.0)
    #finalaudio = video_editor.CompositeAudioClip([clip.audio, audio])
    clip = clip.set_audio(audio)
    return clip




#y = hotsub()
#pre_processing(y)
#print(y)
#tts(y)
f = cut_one_min("m.mp4")
d = create_video(f ,"01.03.2023.mp3")
d.write_videofile("final.mp4")
#test = cut_ten_Sekunden("m.mp4")
#test.write_videofile("final.mp4")
print("done")