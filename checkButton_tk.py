from tkinter import *
root=Tk()
root.title("CheckButton")
def var_status():
        print("Hobby 1 : %d\n Hobby 2 : %d"%(var2.get(),var2.get()))
var1=IntVar()
c1=Checkbutton(root,text="Hobby 1",variable=var1)
var2=IntVar()
c2=Checkbutton(root,text="Hobby 2",variable=var2)
b=Button(root,text="Submit",command=var_status)

c1.pack(side=LEFT)
c2.pack(side=LEFT)
b.pack(side=LEFT)
