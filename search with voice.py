import webbrowser as wb
from functions import speak
from functions import get_audio
a=get_audio()
speak('thats the results from a search')
URL1='https://www.google.com/search?q='
wb.open(URL1+a)
