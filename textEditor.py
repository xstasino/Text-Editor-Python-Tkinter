from tkinter import*
from tkinter.filedialog import*

win =Tk()
win.title("My Text Editor")
win.geometry("400x200")
win.resizable(True, True)

def version():
    win1 = Tk()
    win1.title("Version 0.1")
    text1 = Label(win1, text="Created by xstasino 2023")
    text1.pack()


def clear():
    keimeno.delete(1.0, END)


def batman():
    if dm.get() == 1:
        keimeno.config(background="black", foreground="white")
    else:
        keimeno.config(background="white", foreground="black")

def save_file():
    filepath = asksaveasfilename(defaultextension="txt",filetypes=[('Text files','.txt'),('Word Document','.Docx')])

    if not filepath:
        return
    with open(filepath,'w') as my_file:
       save_keimeno =  keimeno.get(1.0,END)
       my_file.write(save_keimeno)

def open_file():
    filepath = askopenfilename(filetypes=[('Text files','.txt'),('Word Document','.Docx')])

    if not filepath:
        return
    with open(filepath, 'r') as my_file:
        open_keimeno = my_file.read()
        keimeno.delete(1.0,END)
        keimeno.insert(END, open_keimeno)




menubar = Menu(win)


filemenu = Menu(menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New file", command= clear)
filemenu.add_command(label="Open", command= open_file)
filemenu.add_command(label="Save", command = save_file)
filemenu.add_command(label="Exit", command=win.destroy)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Copy", command=lambda: win.event_generate('<Control-c>'))
editmenu.add_command(label="Cut", command=lambda: win.event_generate('<Control-x>'))
editmenu.add_command(label="Paste", command=lambda: win.event_generate('<Control-v>'))
menubar.add_cascade(label="Edit", menu=editmenu)

dm = IntVar()
viewmenu = Menu(menubar)
viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_checkbutton(label="Darkmode", variable=dm, command=batman)
menubar.add_cascade(label="View", menu=viewmenu)

helpmenu = Menu(menubar)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="about", command = version)
menubar.add_cascade(label="Help", menu=helpmenu)

win.config(menu=menubar)

keimeno = Text(win)
keimeno.pack()


win.mainloop()