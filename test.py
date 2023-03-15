import autosub
import moviepy.editor
import ffmpeg
import subprocess
import speech_recognition as sr
import requests

#subprocess.run(" cd C:\\Python311\\Scripts && autosub C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot\\15.03.2023.mp3" , shell=True)
#subprocess.run(" cd C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot && subtitle-editor 11.03.2023.final.mp4 11.03.2023.final.srt" , shell=True)

import speech_recognition as sr
import datetime
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

# Define the input and output file paths
#subprocess.run(['ffmpeg', '-i','15.03.2023.mp3' , '15.03.2023.wav'])
date = datetime.datetime.now()
mp3 = ".mp3"
mp4 = ".mp4"
srt = ".srt"
zus_audio_name = date.strftime("%d.%m.%Y") + mp3
zus_video_name = date.strftime("%d.%m.%Y") + mp4
zus_srt_name   = date.strftime("%d.%m.%Y") + srt
final_video_name = date.strftime("%d.%m.%Y") + ".final" + mp4 


input_file = "C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot\\" + zus_audio_name
output_file = r"C:\Users\nourm\OneDrive\Desktop\Nour\Bot" +zus_srt_name
email = "rbot629@gmail.com"
def get_srt():
    s = Service("chromedriver.exe")
    webDriver = webdriver.Chrome( service = s )
    webDriver.get("https://www.subtitlevideo.com/")
    webDriver.implicitly_wait(10)
    language_Butten = webDriver.find_element(By.ID , "language_in")
    language_Butten.send_keys("en-US")
    
    upload_Butten = webDriver.find_element(By.ID , "fileToUpload")
    upload_Butten.send_keys(input_file)
    
    row_progress_Butten = webDriver.find_element(By.XPATH , "/html/body/div[2]/div/form/fieldset/div[4]")
    while(int(row_progress_Butten.text.replace("%",""))<100):
        time.sleep(1)
    
    email_Butten = webDriver.find_element(By.ID , "email")
    email_Butten.send_keys(email)
    
    convert_video_Butten = webDriver.find_element(By.ID , "convert_video")
    convert_video_Butten.click()
    
    convert_video_done_Butten = webDriver.find_element(By.XPATH , "/html/body/div[2]/div/div[4]/div[3]/table/tr[2]/td[5]")
    
    while(convert_video_done_Butten.text != "done"):
        time.sleep(10)
    

    time.sleep(5)
    
    print("this is the sit u want to print:"+row_progress_Butten.text)
    
    


get_srt()
print("done")

"""
# Create a speech recognition object
r = sr.Recognizer()

def get_large_audio_transcription(path):
    
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks

    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text

print("\nFull text:", get_large_audio_transcription(input_file))

"""