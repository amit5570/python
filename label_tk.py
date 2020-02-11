from tkinter import *
root=Tk()
root.title("LABEL")
def disply():
        print('Name '+ent1.get())
l1=Label(root,text="Enter Name: ")
ent1=Entry(root)
b1=Button(root,text="Submit",command=disply,bg="black",fg="white")
l1.grid(row=0,column=0)
ent1.grid(row=0,column=1)
b1.grid(row=1,columnspan=2)
