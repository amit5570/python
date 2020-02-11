from tkinter import *
root=Tk()
def display():
    print(lst.get(ACTIVE))

lst=Listbox(root)
lst_ent=("Data 1","data 2","data 3","data 4","data 5","data 6")
for v in lst_ent:
    lst.insert(END,v)
b=Button(root,text="Get",command=display)
del_index=int(input('enter index to delete: '))
lst.delete(del_index)
lst.pack()
b.pack()
