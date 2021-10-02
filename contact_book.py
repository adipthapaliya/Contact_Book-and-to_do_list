
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk



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
    add_window=Toplevel(root)
    add_window.geometry("300x300")
    add_window.resizable(False,False)
    #==================     Input Box   ==================================

    def submit():
        #=====database
        conn=sqlite3.connect('contact.db')
        c=conn.cursor()

        #insert to table
        c.execute("INSERT INTO phonebook VALUES(:name, :phonenumber, :adress)",
        
                {
                    "name": add_name_entry.get(),
                    "phonenumber": add_phonenumber_entry.get(),
                    "adress": add_adress_entry.get()
                    
                }
        
        )

        conn.commit()
        conn.close()


        messagebox.showinfo("Contact record","Contact added successfully")

        add_window.destroy()
    

    def cancle():
        add_window.destroy()

    
    add_name_label=Label(add_window,text="Name")
    add_name_label.grid(row=0,column=0,pady=10)

    add_name_entry=Entry(add_window,width=30)
    add_name_entry.grid(row=0,column=1,pady=10)

    add_phonenumber_label=Label(add_window,text="Phone number")
    add_phonenumber_label.grid(row=1,column=0)

    add_phonenumber_entry=Entry(add_window,width=30)
    add_phonenumber_entry.grid(row=1,column=1)

    add_adress_label=Label(add_window,text="Adress")
    add_adress_label.grid(row=2,column=0,pady=10)

    add_adress_entry=Entry(add_window,width=30)
    add_adress_entry.grid(row=2,column=1,pady=10)

    submit_button=Button(add_window,text="Submit",command=submit)
    submit_button.grid(row=3,column=0,pady=30)

    cancle_button=Button(add_window,text="Cancle",command=cancle)
    cancle_button.grid(row=3,column=1,pady=30)


def refresh_window():
    for ele in secondary_frame.winfo_children():
        ele.destroy()
    
    display_frame()



def close_window():
    root.destroy()



def delete_user():
    delwin=Toplevel(root)
    delwin.title("Delete records")



    ###delete function
    def delete():
        conn=sqlite3.connect('contact.db')
        c=conn.cursor()


        c.execute("DELETE FROM phonebook WHERE oid= "+ del_box.get())

        del_box.delete(0,END)

        conn.commit()
        conn.close()

        messagebox.showinfo("Contact Record","Contact deleted sucessfully")

        delwin.destroy()




    del_box=Entry(delwin,width=20)
    del_box.grid(row=0,column=1,padx=20,pady=5)

    del_label=Label(delwin,text="User ID")
    del_label.grid(row=0,column=0,padx=10,pady=5)

    delete_button=Button(delwin,text="Delete User ID",command=delete)
    delete_button.grid(row=8,column=0,columnspan=2,padx=10,pady=10)





def update_contact():

    conn=sqlite3.connect('contact.db')
    c=conn.cursor()

    record_id=edit_box.get()

    c.execute("""UPDATE phonebook SET
            name = :user,
            phonenumber = :number,
            adress = :adress

            WHERE oid= :oid""",
        
        {
            "user": edit_name_entry.get(),
            "number": edit_phonenumber_entry.get(),
            "adress":edit_adress_entry.get(),

            "oid":record_id



        }
        
        )


    conn.commit()
    conn.close()

    messagebox.showinfo("Update","Contact updated sucessfully")

    editwin.destroy()







def edit_window():

    global editwin

    editwin=Toplevel(root)
    editwin.title("Edit records")
    editwin.geometry('300x300')

    def cancle():
        editwin.destroy()  


    def edit():
        
        edit_name_entry.delete(0,END)
        edit_phonenumber_entry.delete(0,END)
        edit_adress_entry.delete(0,END)
        

        conn=sqlite3.connect('contact.db')
        c=conn.cursor()



        employeid=edit_box.get()
        c.execute("SELECT * FROM phonebook WHERE oid="+ employeid)
        records=c.fetchall()
        for record in records:
            edit_name_entry.insert(0,record[0])
            edit_phonenumber_entry.insert(0,record[1])
            edit_adress_entry.insert(0,record[2])
        

        conn.commit()
        conn.close()
   



    ########all box and level
    #######making global

    global edit_name_entry
    global edit_phonenumber_entry
    global edit_adress_entry
    global edit_box

    edit_name_label=Label(editwin,text="Name")
    edit_name_label.grid(row=2,column=0,pady=10)

    edit_name_entry=Entry(editwin,width=30)
    edit_name_entry.grid(row=2,column=1,pady=10)

    edit_phonenumber_label=Label(editwin,text="Phone number")
    edit_phonenumber_label.grid(row=3,column=0)

    edit_phonenumber_entry=Entry(editwin,width=30)
    edit_phonenumber_entry.grid(row=3,column=1)

    edit_adress_label=Label(editwin,text="Adress")
    edit_adress_label.grid(row=4,column=0,pady=10)

    edit_adress_entry=Entry(editwin,width=30)
    edit_adress_entry.grid(row=4,column=1,pady=10)

    submit_button=Button(editwin,text="Submit",command=update_contact)
    submit_button.grid(row=5,column=0,pady=30)

    cancle_button=Button(editwin,text="Cancle",command=cancle)
    cancle_button.grid(row=5,column=1,pady=30)

    #====submit

   

    edit_box=Entry(editwin,width=20)
    edit_box.grid(row=0,column=1,padx=20,pady=5)

    edit_label=Label(editwin,text="User ID")
    edit_label.grid(row=0,column=0,padx=10,pady=5)

    edit_button=Button(editwin,text="Edit User ID",command=edit)
    edit_button.grid(row=1,column=0,columnspan=2,padx=10,pady=10)


#====================================================        GUI     ============================================================

    #==================  Frames

function_frame=Frame(root)
function_frame.place(x=580,y=0,height=400,width=120)








add_button=Button(function_frame,text="Add",padx=40,command=add_contact)
add_button.grid(row=0,column=0,padx=5,pady=20)

delete_button=Button(function_frame,text="Delete",padx=40,command=delete_user)
delete_button.grid(row=1,column=0,padx=5)

update_button=Button(function_frame,text="Update",padx=40,command=edit_window)
update_button.grid(row=2,column=0,padx=5,pady=20)

refresh_button=Button(function_frame,text="Refresh",padx=40,command=refresh_window)
refresh_button.grid(row=3,column=0,padx=5)


exit_button=Button(function_frame,text="Exit",padx=40,command=close_window)
exit_button.grid(row=4,column=0,padx=5,pady=170)


def display_frame():

    global secondary_frame


            #----------------    Creating a Frame  --------------------------

    secondary_frame = Frame(root,bg="#ffffff",highlightbackground="black",highlightthickness=1)
    secondary_frame.place(x=0, y=20)

    my_canvas = Canvas(secondary_frame, width=550, height=390,bg="#ffffff")
    my_canvas.pack(side=LEFT, fill=BOTH)

    my_scrollbar = ttk.Scrollbar(secondary_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, padx=2, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))        

    second_frame = Frame(my_canvas, width=550, height=400,bg="#ffffff")


    my_canvas.create_window((0,0), window=second_frame)

    #------------------------    using database to display contact      -----------------------

    id_label=Label(second_frame,text="ID")
    id_label.grid(row=0,column=0)

    name_label=Label(second_frame,text="Name",padx=40)
    name_label.grid(row=0,column=1)

    phonenumber_label=Label(second_frame,text="Phone no",padx=40)
    phonenumber_label.grid(row=0,column=3)

    adress_label=Label(second_frame,text="Adress",padx=40)
    adress_label.grid(row=0,column=4)

    conn=sqlite3.connect('contact.db')
    c=conn.cursor()

    c.execute("SELECT *,oid FROM phonebook")
    records=c.fetchall()
    

    
    i=1
    for record in records:
        id_labels=Label(second_frame,text=record[3])
        id_labels.grid(row=i,column=0)

        name=Label(second_frame,text=record[0],padx=40)
        name.grid(row=i,column=1)

        phonenumber=Label(second_frame,text=record[1],padx=40)
        phonenumber.grid(row=i,column=3)

        adress=Label(second_frame,text=record[2],padx=40)
        adress.grid(row=i,column=4)

        i+=1

    
    conn.commit()
    conn.close()

     


display_frame()


conn.commit()
conn.close()

root.mainloop()