from tkinter import *
root=Tk()
root.title("Title Here ")
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
print("screen width",w)
print("screen height",h)
root.geometry("500x500+100+200")
root.mainloop()
