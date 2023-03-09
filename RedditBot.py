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

video_editor.ImageMagickPath = "C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"

engine = pyttsx3.init()
date = datetime.datetime.now()
mp3 = ".mp3"
mp4 = ".mp4"
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

        #git Comment
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

# can you pass a video?? das kann das problem sein vllt mach alles in eine methode!
def create_final_video(video, subaudio):
    audio = video_editor.AudioFileClip(subaudio)
    clip = video_editor.VideoFileClip(video)
    #subtitle = video_editor.TextClip(fs, fontsize=30, color='white', bg_color='black').set_pos('center')
    #subtitle = subtitle.set_duration(audio.duration)
    clip = clip.volumex(0.0)
    clip = clip.set_audio(audio)
    #clip = video_editor.CompositeVideoClip([clip,subtitle])
    clip.write_videofile(final_video_name)
    clip.close()
    #lösch den background_video muss noch gemacht werden
    


#funktioniert nicht obwohl ich alles schliße. Es kommt diese fehler [WinError 32] Der Prozess
#kann nicht auf die Datei zugreifen, da sie von einem anderen Prozess verwendet wird
#def delete_background_video(name):
    #path = os.path.abspath(name)
    #print(path)
    #video_editor.VideoClip.close(name)
    #os.remove(path)

def video_with_subtitels():
    s = Service("chromedriver.exe")
    webDriver = webdriver.Chrome( service = s )
    webDriver.get("https://www.veed.io/login")
    webDriver.implicitly_wait(10)
    email = "rbot629@gmail.com"
    passwort = "123poi??"
    def login():
        #das funktioniert nicht weil es immer eine neue fenster name erstellt
        cookies_Butten = webDriver.find_element(By.ID , "onetrust-accept-btn-handler")
        cookies_Butten.click()
        login_Butten = webDriver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[1]/div/div[1]/form/div[1]/button")
        login_Butten.click()
        webDriver.switch_to._w3c_window("https://accounts.google.com/o/oauth2/v2/auth/identifier?gsiwebsdk=3&client_id=53533895812-ghiehgb03dtruurb1caasu8ko8qdtpld.apps.googleusercontent.com&scope=openid%20profile%20email%20email&redirect_uri=storagerelay%3A%2F%2Fhttps%2Fwww.veed.io%3Fid%3Dauth266303&prompt=consent&access_type=offline&response_type=code&include_granted_scopes=true&enable_serial_consent=true&service=lso&o2v=2&flowName=GeneralOAuthFlow")
        mailfeld = webDriver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        mailfeld.send_keys(email)
    login()
    time.sleep(10)





y = hotsub()
#pre_processing(y)
print(y)
#tts(y)
print("hier ist die subtest " + submissionList[SubTest].url)
print("hier ist die subtest " + c.id)
#make_suitable_background_video(get_thirty_minute_video())
#create_final_video(zus_video_name, zus_audio_name)
#video_with_subtitels()
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




"""
def testst():
    
    sub = SubtitlesClip("06.03.2023.final.srt")
    
    z  = ""
    z = str(sub)
    print(sub) 
    stl = [] 
    stl2 = []
    stl3 = []
    stl = z.split(" ")    
    # Erstellen einer Liste von Listen
    stl2 = [x.split("\n") for x in stl]
    # Erstellen einer flachen Liste
    stl3 = [element for inner_list in stl2 for element in inner_list]
    zahlen_liste = []
    for element in stl3:
        if element.isnumeric() or (element.count(".") == 1 and element.replace(".", "").isnumeric()):
            zahlen_liste.append(float(element))
    # String in Zeilen aufteilen
    zeilen = z.split("\n")

    # Letzte Zeilen auswählen und in eine Liste kopieren
    letzte_zeilen = [zeile for zeile in zeilen if zeile.endswith(",") or zeile.endswith(".") or zeile.endswith("\"")]
    print(letzte_zeilen)
    
    
    #subtitle = video_editor.TextClip(fs, fontsize=30, color='white', bg_color='black').set_pos('top')
    #subtitle = subtitle.set_duration(v.duration)
    #v = video_editor.VideoFileClip("06.03.2023.final.mp4")
    #final = video_editor.CompositeVideoClip([v, sub])
    #final.write_videofile("final10000.mp4", fps=v.fps)

def testst():
    srt_file = "06.03.2023.final.srt"
    video_file = "06.03.2023.final.mp4"
    video = VideoFileClip(video_file)
    
    subs = pysrt.open(srt_file)
    
    if len(subs) > 0:
        # Verarbeiten Sie den Inhalt der SRT-Datei
        fps = video.fps  # Beispiel-FPS für das Video
        subs_list = [(((sub.start.ordinal / 1000), (sub.end.ordinal / 1000)), sub.text.replace('\n', ' ')) for sub in subs]
    else:
        print('Die SRT-Datei ist leer oder konnte nicht geöffnet werden.')
        return

    subtitles = SubtitlesClip(subs_list, video.size)
    subtitles = subtitles.set_position(('center', 'bottom'))

    video_with_subtitles = video.set_audio(None).set_duration(subtitles.duration)
    video_with_subtitles = video_with_subtitles.set_fps(fps)
    video_with_subtitles = video_with_subtitles.add_audio(video.audio)

    final_video = video_with_subtitles.set_audio(video.audio)
    final_video = final_video.set_duration(video.duration)
    final_video = final_video.set_fps(fps)

    final_video.write_videofile('example_with_subtitles.mp4', audio_codec='aac')

"""

