import datetime
import os
import math
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
mp4 = ".mp4"
zus_audio_name = date.strftime("%d.%m.%Y") + mp3
zus_video_name = date.strftime("%d.%m.%Y") + mp4
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
    x.save(zus_audio_name)

def get_audio():
    #hier musst du die sub aufrufen damit du den name bekommst
    return video_editor.AudioFileClip("01.03.2023.mp3")
   
def make_suitable_background_video(video):
    audio = get_audio()
    start = random.randrange(1, 1800)
    #Bestimmt wie viel Sekunden ausm video genommen werden
    ende  = start + math.ceil(audio.duration) 
    cur = video_editor.VideoFileClip(video).subclip(start, ende)
    cur.write_videofile(zus_video_name)
    

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


# can you pass a video?? das kann das problem sein vllt mach alles in eine methode 
# wenn das nicht geht: mach einfach "die add_ten_sekunden" weg und stat "cut_one_min" mach eine mehtode die
# dirkt nach die länge des audios ein video erstelt und speichert mit dem datum als name 
def create_final_video(video):
    #audio = video_editor.AudioFileClip(subaudio)
    audio = get_audio()
    clip = video_editor.VideoFileClip(video)
    clip = clip.volumex(0.0)
    clip = clip.set_audio(audio)
    clip.write_videofile("final.mp4")
    #lösch den background_video
    os.remove(zus_video_name)





#y = hotsub()
#pre_processing(y)
#print(y)
#tts(y)
make_suitable_background_video("m.mp4")
create_final_video(zus_video_name)
print("done")