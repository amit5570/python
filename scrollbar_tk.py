from tkinter import *
root=Tk()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
lst=Listbox(root,yscrollcommand=s.set)
for i in range(0,50):
    lst.insert(END,i)
lst.pack(side=LEFT,fill=BOTH)
s.config(command=lst.yview)
