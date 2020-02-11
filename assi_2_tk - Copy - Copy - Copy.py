from tkinter import *
root=Tk()
root.title=("python GUI")
l1=Label(root,text="Enter a name: ")
l2=Label(root,text="Choose a number: ")
ent=Entry(root)
n1=StringVar()
num=Spinbox(root,width=12,textvariable=n1)
