from tkinter import *
import time
window=Tk()
window.title("homa")
label=Label(window,text="Hey!!!",fg='green',height=50,width=50,bg='white',font=('Times New Roman',80))
label.pack()
time.sleep(3.0)
label2=Label(window,text="Please type or speak...",fg='green',height=50,width=50,bg='white',font=('Times New Roman',50),anchor=SW)
label2.pack()
window.mainloop()
