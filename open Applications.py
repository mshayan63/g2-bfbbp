import os
from functions import speak
from functions import get_audio
a=get_audio()
b=a.split(" ")
if 'please'==b[-1]:
        b.pop()
a=b.pop()
os.startfile(a)
