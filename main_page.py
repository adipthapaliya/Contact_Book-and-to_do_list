from tkinter import *
from PIL import ImageTk, Image
import subprocess

root=Tk()
root.title("Home")
root.geometry('700x400')
root.resizable(False,False)


def open_contactbook():
    root.destroy()
    subprocess.call(["python","contact_book.py"])

def open_todolist():
    root.destroy()
    subprocess.call(["python","to_do_list.py"])

#-------------------------------------      Icon      ------------------------------

contact_image=Image.open("Icon/contact_icon.png")
todolist_image=Image.open("Icon/todo_icon.png")

contact_image= contact_image.resize((100,100),Image.ANTIALIAS)
todolist_image= todolist_image.resize((100,100),Image.ANTIALIAS)

contact_icon= ImageTk.PhotoImage(contact_image)
todo_icon= ImageTk.PhotoImage(todolist_image)



contact_button=Button(root,image=contact_icon,borderwidth=0,command=open_contactbook)
contact_button.place(x=230,y=120)

todo_button=Button(root,image=todo_icon,borderwidth=0,command=open_todolist)
todo_button.place(x=370,y=120)



root.mainloop()