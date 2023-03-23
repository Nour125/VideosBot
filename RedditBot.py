import datetime
import glob
import os
import math
import time
import pysrt
import pyttsx3
import random
import gtts
from playsound import playsound
from gtts.tokenizer import pre_processors
import moviepy.editor as video_editor
import praw
from praw.models import MoreComments
from wand.image import Image
import wand.api
from moviepy.video.tools.subtitles import SubtitlesClip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ffmpeg
import subprocess


video_editor.ImageMagickPath = "C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"

engine = pyttsx3.init()
date = datetime.datetime.now()
mp3 = ".mp3"
mp4 = ".mp4"
srt = ".srt"
zus_audio_name = date.strftime("%d.%m.%Y") + mp3
zus_video_name = date.strftime("%d.%m.%Y") + mp4

final_video_name = date.strftime("%d.%m.%Y") + ".final" + mp4 
commentsList = []
submissionList = []
commentwords = list()
thirty_minute_videos = ["minecraft.mp4","Rocket_League.mp4"]
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
        for submission in subReddit.hot(limit = 10):
            submissionList.append(submission) 
        
        x = random.randrange(10)
        if(submissionList[x].over_18 == True):
            sub = "NSFW" + submissionList[x].title
        else:
            sub = submissionList[x].title
        cursub = submissionList[x] # du brauchst es für die screanshot vom title wie weiss ich noch nicht :(
        global SubTest
        SubTest = x

        #get Comment
        cursub.comments.replace_more(limit = 0)
        #submission.comment_sort = "new"  #Macht iwie nichts :(
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
        
        global c
        c = topcom

        if ((i+1) == len(commentsList)):
            subfound = False
        else:
            subfound = True

    reddit.read_only = False  
    global fs
    fs = sub +"\n"+ com
    return (fs)


def pre_processing(text):
    t = pre_processors.tone_marks(text)
    t = pre_processors.end_of_line(t)
    t = pre_processors.abbreviations(t)
    t = pre_processors.word_sub(t)
    return t

def tts (text):
    x = gtts.gTTS(text, lang ='en', tld ='us')
    x.save(zus_audio_name)

def get_audio():
    #hier musst du die sub aufrufen damit du den name bekommst
    return video_editor.AudioFileClip(zus_audio_name)

def get_thirty_minute_video():
    r = random.randrange( 0 , len(thirty_minute_videos) )
    return thirty_minute_videos[r]
   
def make_suitable_background_video(video):
    audio = video_editor.AudioFileClip(zus_audio_name)
    start = random.randrange(1, 1800)
    #Bestimmt wie viel Sekunden ausm video genommen werden
    ende  = start + math.ceil(audio.duration) 
    cur = video_editor.VideoFileClip(video).subclip(start, ende)
    cur.write_videofile(zus_video_name)
    cur.reader.close()
    cur.close()    

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

def get_srt():
    email = "bopaxi6270@kaudat.com"
    s = Service("chromedriver.exe")
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : r"C:\Users\nourm\OneDrive\Desktop\Nour\Bot"}
    chromeOptions.add_experimental_option("prefs",prefs)
    webDriver = webdriver.Chrome( service = s, options = chromeOptions )
    

    webDriver.get("https://www.subtitlevideo.com/")
    webDriver.implicitly_wait(20)
    
 
    language_Butten = webDriver.find_element(By.ID , "language_in")
    language_Butten.send_keys("English (United States)-English (United States)")

    upload_Butten = webDriver.find_element(By.ID , "fileToUpload")
    input_file = "C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot\\" + zus_audio_name
    upload_Butten.send_keys(input_file)
    
    row_progress_Butten = webDriver.find_element(By.XPATH , "/html/body/div[2]/div/form/fieldset/div[4]")
    while(int(row_progress_Butten.text.replace("%",""))<100):
        time.sleep(10)
    
    email_Butten = webDriver.find_element(By.ID , "email")
    email_Butten.send_keys(email)
    
    convert_video_Butten = webDriver.find_element(By.ID , "convert_video")
    convert_video_Butten.click()
    time.sleep(60)
    
    convert_video_done_Butten = webDriver.find_element(By.LINK_TEXT , "en-US subtitles")

    global zus_srt_name
    zus_srt_name =  convert_video_done_Butten.get_attribute('href').removeprefix("https://files.subtitlevideo.com/subtitles/")
    convert_video_done_Butten.click()
    time.sleep(10)


# command to add subtitle to video and create a new video with subtitle
def add_subtitles(video, subtitles):
    l = "subtitles="+subtitles+":force_style='Alignment=10,Fontsize=24,MarginV=20'"
    subprocess.run(['ffmpeg', '-i', video, '-vf', l,
                        '-c:a', 'copy', 'video_with_subtitle.mp4'])
    
    
  


# can you pass a video?? das kann das problem sein vllt mach alles in eine methode!
def create_final_video(video, subaudio, subtitles):
    audio = video_editor.AudioFileClip(subaudio)
    add_subtitles(video,subtitles)
    clip = video_editor.VideoFileClip("video_with_subtitle.mp4")
    clip = clip.volumex(0.0)
    clip = clip.set_audio(audio)
    clip.write_videofile(final_video_name)
    video_editor.VideoFileClip(clip).close()
    audio.close()
   


#du willst ja nicht alles löschen bis auf das end produtk
def delete_unnecessary_stuff():
    delsrt = "del /f " + zus_srt_name
    delv   = "del /f " + zus_video_name
    dela   = "del /f " + zus_audio_name

    subprocess.run(delsrt , shell=True, check=True)
    subprocess.run(delv, shell=True, check=True)
    subprocess.run(dela, shell=True, check=True)
    subprocess.run("del /f video_with_subtitle.mp4", shell=True, check=True)




y = hotsub()
doentext = pre_processing(y)
print(y)
print(doentext)
tts(doentext)
print("hier ist die subtest " + submissionList[SubTest].url)
print("hier ist die subtest " + c.id)
make_suitable_background_video(get_thirty_minute_video())
get_srt()
create_final_video(zus_video_name, zus_audio_name, zus_srt_name)
delete_unnecessary_stuff()
print("done")

# diese ist dafür da das ich einmal pro Tag poste

def main():
    while(True):
        #mach was du willst

        day = datetime.datetime.now
        day = day + datetime.timedelta(days = 1)
        while(datetime.date.day() == day ):
            #einfach warten bis der nächte tag kommt dann nochmla was posten
            x = x




