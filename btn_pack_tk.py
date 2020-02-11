from tkinter import *
root=Tk()
root.title("Button")
def call():
        print('Clicked!!')

b1=Button(root,text="button one",command=call,bg="red",fg="white")
b2=Button(root,text="button two",command=call,bg="green",fg="black")
b1.pack()
b2.pack()
