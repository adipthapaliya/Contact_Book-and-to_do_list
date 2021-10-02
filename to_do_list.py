from tkinter import *
from tkinter.font import Font 
import subprocess  
from tkinter import filedialog
import pickle

root=Tk()
root.title("To Do List")
root.geometry('700x400')
root.resizable(False,False)


def add_entry():

    global addwin

    addwin=Toplevel(root)
    addwin.title("Add")
    addwin.geometry('300x300')
    addwin.resizable(False,False)

    def add_iteam():
        todo_list.insert(END, add_entrybox.get())
        addwin.destroy()

    def cancle():
        addwin.destroy() 

    add_entrybox=Entry(addwin,font=("Helvetica",15),width=27)
    add_entrybox.grid(row=0,column=0,columnspan=2,ipady=30)

    done_button=Button(addwin,text="Done",command=add_iteam)
    done_button.grid(row=1,column=0)

    cancle_button=Button(addwin,text="Cancle",command=cancle)
    cancle_button.grid(row=1,column=1) 

def delete_iteam():
    todo_list.delete(ANCHOR)



def save_iteam():
    file_name= filedialog.asksaveasfilename(

        initialdir="E:\Computing\Project\Contact_Book\data",
        title="Save File",
        filetypes=(("Dat Files","*.dat"),
                    ("All Files","*.*"))
    )

    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name=f"{file_name}.dat"

    
    tosave_list=todo_list.get(0,END)
    output_file=open(file_name,"wb")

    pickle.dump(tosave_list,output_file)

def open_iteam():
    file_name = filedialog.askopenfilename(
        
        initialdir="E:\Computing\Project\Contact_Book\data",
        title="Open File",
        filetypes=(("Dat Files","*.dat"),
                    ("All Files","*.*"))
    )

    if file_name:
        todo_list.delete(0,END)

        saved_file =open(file_name,"rb")

        saved_list=pickle.load(saved_file)

        for iteam in saved_list:
            todo_list.insert(END,iteam)


def close_window():
    root.destroy()
    subprocess.call(["python","main_page.py"])




my_font=Font(
    family="Arial",
    size=15


)


# creating frame
main_frame=Frame(root,highlightbackground="black",highlightthickness=1)
main_frame.place(x=0,y=0)

function_frame=Frame(root)
function_frame.place(x=570,y=0,height=400,width=127)

open_button=Button(function_frame,padx=30,text="Open",command=open_iteam)
open_button.grid(row=0,column=0,padx=5,pady=20)

save_button=Button(function_frame,text="Save",padx=30,command=save_iteam)
save_button.grid(row=1,column=0,padx=5)

add_text_button=Button(function_frame,padx=30,text="Add Item",command=add_entry)
add_text_button.grid(row=2,column=0,padx=5,pady=20)

delete_button=Button(function_frame,text="Delete Item",padx=30,command=delete_iteam)
delete_button.grid(row=3,column=0,padx=5)



exit_button=Button(function_frame,text="Exit",padx=40,command=close_window)
exit_button.grid(row=4,column=0,padx=5,pady=170)





todo_list= Listbox(main_frame,
    font=my_font,
    width=50,
    height=16,
    bd=0,
    selectbackground="#a6a6a6",
    activestyle="none"



)

todo_list.pack(side=LEFT,fill=BOTH)


defult_list=[ ]

for work in defult_list:
    todo_list.insert(END,work)


#-----------------------------      for scroll bar      ------------------

scroll=Scrollbar(main_frame)
scroll.pack(side=RIGHT,fill=BOTH)

todo_list.config(yscrollcommand=scroll.set)
scroll.config(command=todo_list.yview)


root.mainloop()