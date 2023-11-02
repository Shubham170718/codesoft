from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("TO-DO-LIST")
root.geometry("400x650")
root.resizable(False,False)

task_list= []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist1.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END , task)  

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist1.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)        

def openTaskFile():
    try:
        global task_list
        with open("tasklist1.txt","r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END ,task)
    except:
        file = open('tasklist1.txt','w')
        file.close()            


# icon
icon = Image.open("todo_logo.jpg")
icon_image= ImageTk.PhotoImage(icon)
root.iconphoto(False,icon_image)

# topbar
Top = Image.open("topbar.jpg",)
Top = Top.resize((400,100))
topbar = ImageTk.PhotoImage(Top)
l1=Label(root,image=topbar)
l1.pack()

todo = Label(root,text="TO-DO",font="italic 30 bold",bg="light blue")
todo.place(x=140,y=50)

heading = Label(root,text="TASKS",font="arial 20 bold",fg="white",bg="green",padx=40)
heading.place(x=100,y=120)

# main
frame= Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=170)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0,bg="gray")
task_entry.place(x=10,y=7)

button= Button(frame,text="ADD",font="arial 20 bold",width=6,bg="blue",fg="white",bd=0,command=addTask)
button.place(x=300,y=0)
task_entry.focus()

# box
frame1 = Frame(root,bd=3,width=700,height=280,bg="gray")
frame1.pack(pady=(140,0))
listbox = Listbox(frame1,font=('arial',12),width=40,height=16,bg="gray",fg="black",cursor="hand2")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side= RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile() # for save the task 


# delete
button1 = Button(root,text="DELETE",bd=0,font="arial 20 bold",fg="white",bg="red",command=deleteTask)
button1.pack(side=BOTTOM,pady=13)

root.mainloop()