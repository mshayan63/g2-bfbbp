import os
import time
import speech_recognition as sr
from gtts import gTTS
import playsound

def speak(text):
	tts = gTTS(text=text,lang="en")
	filename = "C:/Users/js/AppData/Local/Programs/Python/Python39/voice.mp3"
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