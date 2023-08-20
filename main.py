import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import os
import shutil
# imported to change software resulotion
import pyautogui

def openFile():
    path = filedialog.askdirectory();

    list_ = os.listdir(path)
   
    for file_ in list_:
        name, ext = os.path.splitext(file_)
    
        ext = ext[1:]
    
        if ext == '':
            continue
    
        if os.path.exists(path+'/'+ext):
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
    
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)


window = tk.Tk()
window.title("Organize files in a directory")
window.geometry("350x400")

text = ttk.Label(text="Select a folder to organize")
text.pack(pady=50)

button = ttk.Button(text="Open folder", command=openFile)
button.pack()

credit = ttk.Label(text="Program created by Noam Levi")
credit.pack(pady=(220,0))

window.mainloop()