import functions
import os
PATH= 'c:/Users/js/Desktop/database.txt'
def validation():
    if not os.path.exists(PATH):
        f = open(PATH, "w+")
        f.write('')
def add(name):
    validation()
    f = open(PATH, "a+")
    new_phone = name 
    f.write(new_phone)
    f.close
functions.speak("please enter your name")
a = input("please enter your name")
add(a)
