import autosub
import moviepy.editor
import ffmpeg
import subprocess


#subprocess.run(" cd C:\\Python311\\Scripts && autosub C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot\\14.03.2023.mp3" , shell=True)
#subprocess.run(" cd C:\\Users\\nourm\\OneDrive\\Desktop\\Nour\\Bot && subtitle-editor 11.03.2023.final.mp4 11.03.2023.final.srt" , shell=True)
(
        ffmpeg
        .input("14.03.2023.final.mp4")
        .filter("subtitles", "subtitles_en-US_33678.srt")
        .output("14.03.20233333333.final.mp4")
        .run()
)

print("done")



"""
(
    ffmpeg
    .input("14.03.2023.final.mp4")
    .filter("subtitles", "14.03.2023.srt")
    .output("output.mp4")
    .run()
)
    if not which("ffmpeg.exe"):
        print("ffmpeg: Executable not found on machine.")
        raise Exception("Dependency not found: ffmpeg")
"""