from tkinter import *
root=Tk()
root.title("Form")

frm=Frame(root)
l1=Label(root,text="Enter Name: ")
l2=Label(root,text="Enter Email: ")
l3=Label(root,text="Enter Contact: ")

name=Entry(root)
email=Entry(root)
contact=Entry(root)

l4=Label(frm,text="Hobbies: ")

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
name.grid(row=0,column=1)
email.grid(row=1,column=1)
contact.grid(row=2,column=1)

frm.grid(row=3,columnspan=2)

c1=Checkbutton(frm,text="Dancing")
c2=Checkbutton(frm,text="Painting")
c3=Checkbutton(frm,text="Reading")

l4.pack(side=LEFT)
c1.pack(side=LEFT)
c2.pack(side=LEFT)
c3.pack(side=LEFT)

btn=Button(frm,text="Submit")
btn.pack(side=BOTTOM)
