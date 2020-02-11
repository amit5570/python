from tkinter import *
root=Tk()
root.title("Title Here ")
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
print("screen width",w)
print("screen height",h)
root.geometry(str(w)+"x"+str(h))
def call():
        print('Clicked!!')

b1=Button(root,text="button one",command=call,bg="red",fg="white")
b2=Button(root,text="button two",command=call,bg="green",fg="black")
b1.place(x=200,y=200)
b2.place(x=300,y=300)

root.mainloop()
