from tkinter import *
root=Tk()
def _quit():
    root.quit()
    root.destroy()
    exit()

menuBar=Menu(root)
root.config(menu=menuBar)
fileM=Menu(menuBar,tearoff=1)
fileM.add_command(label="New")
fileM.add_separator()
fileM.add_command(label="Exit",command=_quit)
menuBar.add_cascade(label="File",menu=fileM)

fileM1=Menu(menuBar)
fileM1.add_command(label="Help")
menuBar.add_cascade(label="About",menu=fileM1)

