import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.iconbitmap(
    r'C:\Users\OLOYA KENNEDY JOSHUA\Desktop\ \PYTHON\PYTHON MODULES\OPERATING SYSTEM\Changa_One\ght.ico')
root.geometry('500x120')
root.title('KnDjoshua')

# check current working directory
cwd = os.getcwd()
print("Current Workind Directory >>>>>> "+cwd)


def getentry():
    confirm = messagebox.askyesno("Proceed", "KnDjoshua")
    if confirm == True:
        global_getit1 = entry1.get()
        global_getit2 = entry2.get()

        # start cpying
        shutil.copytree(global_getit1, global_getit2)
        quit()
    else:
        quit()


entry1 = Entry(root, width=100)
entry1.insert(0, "Enter Source Path")
entry1.config(fg='red')
entry1.pack()

label = Label(root, text="🥷🥷🥷🥷🥷🥷🥷🥷🥷🥷🥷🥷 🥷🥷🥷🥷🥷🥷🥷🥷🥷🥷",font=(40))
label.pack()

entry2 = Entry(root, width=100)
entry2.insert(0, "Enter Destination Path")
entry2.config(fg='red')
entry2.pack()


button = ttk.Button(text="Execute", width=40, command=getentry)
button.pack(pady=10, padx=20)

root.mainloop()
