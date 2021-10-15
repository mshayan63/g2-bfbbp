from functions import speak
from functions import get_audio
#question 1
text = get_audio()
if "how are you" in text:
	speak("fine thanks what about you?")
	text = get_audio()
	if "not bad" in text or "well" in text or "not" not in text and "good" in text or "perfect" in text:
		speak("thats perfect!")
	else:
		speak("do you want to make you happy?")
		text = get_audio()
		if "yes" in text or "yea" in text or "yeap" in text or "yeah" in text:
			speak("i dont have any jokes to tell you. ha. ha ha. ha")
#question 2
elif text == "what's my name" or text == "do you know my name" or text == "what is my name" or "what's my name" in text:
	speak("dont know do you want to tell that?")
	text = get_audio()
	if "yes" in text or "yea" in text or "yeap" in text or "yeah" in text:
		speak("so tell that")
		text = get_audio()
		if "my name is" in text or "its" in text:
			speak("i cant uderstand that please just tell your name")
		text = get_audio()
		speak("hello")
		speak(text)
	elif "no" in text:
		speak("hahaha")
	else: 
		speak("please ask 1 question and answer my question")

