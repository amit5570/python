from tkinter import *
root=Tk()
v=IntVar()
v.set(0)
lst=[('Python',0),('wp',1),('jQuery',2),('Javascript',3)]
def showchoice():
    print('you have selected:',v.get())

lbl=Label(root,text="select your favorite programming lang")
lbl.pack()

for txt,val in lst:
    r=Radiobutton(root,text=txt,variable=v,command=showchoice,value=val)
    r.pack()
