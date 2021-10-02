from tkinter import *
from tkinter.font import Font   

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

    def cancle():
        addwin.destroy() 

    add_entrybox=Entry(addwin,font=("Helvetica",15),width=27)
    add_entrybox.grid(row=0,column=0,columnspan=2,ipady=30)

    done_button=Button(addwin,text="Done")
    done_button.grid(row=1,column=0)

    cancle_button=Button(addwin,text="Cancle",command=cancle)
    cancle_button.grid(row=1,column=1) 


my_font=Font(
    family="Arial",
    size=15


)


# creating frame
main_frame=Frame(root,highlightbackground="black",highlightthickness=1)
main_frame.place(x=0,y=0)

function_frame=Frame(root)
function_frame.place(x=570,y=0,height=400,width=127)


add_text_button=Button(function_frame,padx=40,text="Add",command=add_entry)
add_text_button.grid(row=0,column=0,padx=5,pady=20)

delete_button=Button(function_frame,text="Delete",padx=40)
delete_button.grid(row=1,column=0,padx=5)



todo_list= Listbox(main_frame,
    font=my_font,
    width=50,
    height=16,
    bd=0,
    selectbackground="#a6a6a6",
    activestyle="none"



)

todo_list.pack(side=LEFT,fill=BOTH)


defult_list=["Go to gym","Take a bath","GO to collage","Do your home work","Sleep"]

for work in defult_list:
    todo_list.insert(END,work)


#-----------------------------      for scroll bar      ------------------

scroll=Scrollbar(main_frame)
scroll.pack(side=RIGHT,fill=BOTH)

todo_list.config(yscrollcommand=scroll.set)
scroll.config(command=todo_list.yview)


root.mainloop()