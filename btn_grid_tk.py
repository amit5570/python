from tkinter import *
root=Tk()
root.title("Button")
def call():
        print('Clicked!!')

b1=Button(root,text="button one",command=call,bg="red",fg="white")
b2=Button(root,text="button two",command=call,bg="green",fg="black")
b3=Button(root,text="button three",command=call,bg="blue",fg="white")
b4=Button(root,text="button four",command=call,bg="yellow",fg="black")
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)

