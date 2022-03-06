from tkinter import *
import random, time

def start():
    x=random.choice(['./img/b.png','./img/b2.png','./img/b3.png','./img/b4.png','./img/b5.png','./img/b6.png',])
    return x

def img(event):
    global b1, b2
    for i in range(30):
        b1=PhotoImage(file=(start()))
        b2=PhotoImage(file=(start()))
        lab1['image']=b1
        lab2['image']=b2
        root.update()
        time.sleep(0.12)

root= Tk()
root.geometry('400x200')
root.title('Game of bones. Start game. Click on board!')
root.resizable(height=False, width=False)
root.iconphoto(True,PhotoImage(file=('./img/icon.png')))
font = PhotoImage(file=('./img/bg.png'))
Label(root,image=font).pack()
lab1=Label(root)
lab1.place(relx=0.3,rely=0.5,anchor=CENTER)
lab2=Label(root)
lab2.place(relx=0.7,rely=0.5,anchor=CENTER)
root.bind('<1>',img)
img('event')
root.mainloop()

