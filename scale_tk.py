from tkinter import *
root=Tk()
s1=Scale(root,from_=0,to=50)
s1.pack()
s2=Scale(root,from_=0,to=50,orient=(HORIZONTAL))
s2.pack()
def get():
    print(s1.get())
    print(s2.get())
b=Button(root,text="Get Value",command=get).pack()
