import datetime
import glob
import os
import re
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
import instagrapi
from PIL import Image

video_editor.ImageMagickPath = "C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"

engine = pyttsx3.init()
date = datetime.datetime.now()
mp3 = ".mp3"
mp4 = ".mp4"
srt = ".srt"
zus_audio_name = date.strftime("%d.%m.%Y") + mp3
zus_video_name = date.strftime("%d.%m.%Y") + mp4
zus_thumbnail_name = date.strftime("%d.%m.%Y") + ".png"
thumbnail_Path = "C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot\\" + zus_thumbnail_name
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
            sub = "NSFW." + submissionList[x].title
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
        
        global selected_comment
        selected_comment = topcom

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
    email = "bopaxi6270@kaudat.com" #gajayiy998@necktai.com #jemixa3308@kaudat.com
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
    clip.close() #du musst diese video schliessen 
    audio.close()
   


#du willst ja nicht alles löschen bis auf das end produtk
def delete_unnecessary_stuff():
    delsrt = "del /f " + zus_srt_name
    delv   = "del /f " + zus_video_name 
    dela   = "del /f " + zus_audio_name #wird nicht gelöscht :(
    delfpng   = "del /f " + zus_thumbnail_name
    delfjpeg   = "del /f " + zus_thumbnail_name.replace(".png",".jpeg")

    subprocess.run(delsrt , shell=True, check=True)
    subprocess.run(delv, shell=True, check=True)
    subprocess.run(dela, shell=True, check=True)
    subprocess.run(delfpng, shell=True, check=True)
    subprocess.run(delfjpeg, shell=True, check=True)
    subprocess.run("del /f video_with_subtitle.mp4", shell=True, check=True)

def get_thumbnail():
    s = Service("chromedriver.exe")
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : r"C:\Users\nourm\OneDrive\Desktop\Nour\Bot"}
    chromeOptions.add_experimental_option("prefs",prefs)
    webDriver = webdriver.Chrome( service = s, options = chromeOptions )

    webDriver.get(submissionList[SubTest].url + selected_comment.id)
    webDriver.implicitly_wait(20)
    
    cookies_Butten = webDriver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[1]/section/div/section[2]/section[1]/form/button")
    cookies_Butten.click()
    time.sleep(10)

    if(submissionList[SubTest].over_18 == False):
        pattern = "[class ^= 'Comment t1_" + selected_comment.id +"']"
        bild = webDriver.find_element(By.CSS_SELECTOR,  pattern)
        bild.screenshot(thumbnail_Path)


def post_video_on_insta():
    ich = instagrapi.Client()
    ich.login('trendingtalks_01', '123poi??')
    video_path = "C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot\\" + final_video_name
    
    if(submissionList[SubTest].over_18 == True):
        thumbnail_path = "C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot\\nsfw.png"
        caption1 = "NSFW. " + submissionList[SubTest].title + "\n\n" + "Follow @trendingtalks_01" + "\n\n" + "#redditpost #redditthreads #redditposts #redditmeme #redditmemes #reddit #redditthreac #redditstories #redditstory #relationshipadvice #askreddit #askredditwoman #askredditman #aita #amitheasshole #justnomil"
        caption = caption1
    else:
        get_thumbnail()
        caption1 = submissionList[SubTest].title + "\n\n" + "Follow @trendingtalks_01" + "\n\n" + "#redditpost #redditthreads #redditposts #redditmeme #redditmemes #reddit #redditthreac #redditstories #redditstory #relationshipadvice #askreddit #askredditwoman #askredditman #aita #amitheasshole #justnomil"
        im1 = Image.open(thumbnail_Path)
        im1 = im1.convert("RGB")
        thumbnail_path = "C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot\\" + date.strftime("%d.%m.%Y") + ".jpeg"
        im1.save(thumbnail_path)
        im1.close()
        caption = caption1

    media = ich.clip_upload(
        video_path,
        caption,
        thumbnail_path,
    )

    





# diese ist dafür da das ich einmal alle 5 studnen zu poste

def main():
    while(True):
        y = hotsub()
        doentext = pre_processing(y)
        tts(doentext)
        make_suitable_background_video(get_thirty_minute_video())
        get_srt()
        create_final_video(zus_video_name, zus_audio_name, zus_srt_name)
        post_video_on_insta()
        time.sleep(500)
        delete_unnecessary_stuff()
        print("done")
        fünf_stunden = 1* 60 * 60
        time.sleep(fünf_stunden)

        """
        day = datetime.datetime.now
        day = day + datetime.timedelta(days = 1)
        while(datetime.date.day() == day ):
            #einfach warten bis der nächte tag kommt dann nochmla was posten
            x = x
        """





main()








"""
y = hotsub()
doentext = pre_processing(y)
print(y)
print("hier ist die subtest " + submissionList[SubTest].url)
print("hier ist die subtest " + selected_comment.id)
print(doentext)
tts(doentext)
make_suitable_background_video(get_thirty_minute_video())
get_srt()
create_final_video(zus_video_name, zus_audio_name, zus_srt_name)
post_video_on_insta()
delete_unnecessary_stuff()
print("done")

"""