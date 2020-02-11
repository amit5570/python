from tkinter import *
root=Tk()
v=IntVar()
v.set(0)
lst=[('option 1',0),('option 2',1),('option 3',2)]

def showchoice():
    txt1='you have selected:'+str(v.get())
    lbl.config(text=txt1)

for txt,val in lst:
    r=Radiobutton(root,text=txt,variable=v,command=showchoice,value=val)
    r.pack()
lbl=Label(root,text="hello")
lbl.pack()
