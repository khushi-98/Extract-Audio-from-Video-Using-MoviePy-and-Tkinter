import moviepy.editor 

from tkinter.filedialog import *


vid= askopenfilename()
video=moviepy.editor.VideoFileClip(vid)

aud=video.audio
aud.write_audiofile("C:\\Users\\bansa\\Desktop\\python_projects\\demo.mp3")

print("----END----")