
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import tkk



#==================================================     Creating a Window    ==============================================

root=Tk()
root.title("Contact Book")
root.geometry('700x400')
root.resizable(False,False)


#=========================================          Creating a Database       ==============================================


conn=sqlite3.connect("contact.db")
c=conn.cursor()

# c.execute("""CREATE TABLE phonebook(

#         name TEXT,
#         phonenumber INTEGER,
#         adress TEXT
#         )

#      """)





#====================================================       Functions       ===============================================


def add_contact():
    pass










#====================================================        GUI     ============================================================

    #==================  Frames

main_frame=Frame(root,highlightbackground="black",highlightthickness=1)
main_frame.place(x=0,y=0,height=400,width=580)

function_frame=Frame(root)
function_frame.place(x=580,y=0,height=400,width=120)




id_label=Label(main_frame,text="ID",highlightbackground="black",highlightthickness=1)
id_label.grid(row=0,column=0)

name_label=Label(main_frame,text="Name",padx=40)
name_label.grid(row=0,column=1)

phonenumber_label=Label(main_frame,text="Phone no",padx=40)
phonenumber_label.grid(row=0,column=3)

adress_label=Label(main_frame,text="Adress",padx=40)
adress_label.grid(row=0,column=4)




add_button=Button(function_frame,text="Add",padx=40,command=add_contact)
add_button.grid(row=0,column=0,padx=5,pady=20)

delete_button=Button(function_frame,text="Delete",padx=40)
delete_button.grid(row=1,column=0,padx=5)

update_button=Button(function_frame,text="Update",padx=40)
update_button.grid(row=2,column=0,padx=5,pady=20)

clear_button=Button(function_frame,text="Clear all",padx=40)
clear_button.grid(row=3,column=0,padx=5,pady=210)


def display_frame():

    global secondary_frame


            #----------------    Creating a Frame  --------------------------

    secondary_frame = Frame(root,bg="#ffffff")
    main_frame.place(x=0, y=90)

    my_canvas = Canvas(main_frame, width=1500, height=740,bg="#ffffff")
    my_canvas.pack(side=LEFT, fill=BOTH)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, padx=5, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

    second_frame = Frame(my_canvas, width=1500, height=740,bg="#ffffff")


    my_canvas.create_window((0,880), window=second_frame)



conn.commit()
conn.close()

root.mainloop()