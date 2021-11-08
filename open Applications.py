import os
import time
import speech_recognition as sr
from gtts import gTTS
import playsound
import time
def speak(text):
	tts = gTTS(text=text,lang="en")
	filename = "C:/Users/Pakrah/AppData/Local/Programs/Python/Python39/voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source :
		audio = r.listen(source)
		said = ""
		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exeption :" + str(e))
	return said

from functions import speak
from functions import get_audio
a=get_audio()
b=a.split(" ")
if 'please'==b[-1]:
        b.pop()
        if 'open'==b[0]:
                b.pop(0)
elif 'please'==b[0]:
        b.pop(0)
        if 'open'==b[0]:
                b.pop(0)
if 'open'==b[0]:
        b.pop(0)
a=b[0]
for i in range(len(b)):
     if i>0:
        a=a+' '+b[i]   
os.startfile(a)
