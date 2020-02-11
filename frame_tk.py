from tkinter import *
root=Tk()
root.title("Frame")
def disply():
        if (ent1==""):
                print("Please Enter Nmae!")
        else:
                print("Name:",ent1.get())
                ent1.focus()
l1=Label(root,text="Enter Name:")
frm=Frame(root)
l1.grid(row=0,column=0)
frm.grid(row=0,column=1)
ent1=Entry(frm)

b=Button(frm,text="submit",command=disply)
ent1.grid(row=0,column=0)
b.grid(row=0,column=1)
