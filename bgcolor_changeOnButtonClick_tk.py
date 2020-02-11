from tkinter import *
root=Tk()
color1="Blue"
color2="Yellow"
color3="Green"
def radcall():
    radSel=radVar.get()
    if radSel==1:
        root.configure(background=color1)
    elif radSel==2:
        root.configure(background=color2)
    elif radSel==3:
        root.configure(background=color3)

radVar=IntVar()
rad1=Radiobutton(root,text=color1,variable=radVar,value=1,command=radcall)
rad1.grid(column=0,row=5,sticky=W)
rad2=Radiobutton(root,text=color2,variable=radVar,value=2,command=radcall)
rad2.grid(column=1,row=5,sticky=W)
rad3=Radiobutton(root,text=color3,variable=radVar,value=3,command=radcall)
rad3.grid(column=2,row=5,sticky=W)



