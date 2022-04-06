from tkinter import *
from tkinter import filedialog
from controller import find_summary
import os

import subprocess as sub


def get_file_path():
    global file_path
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
    l1 = Label(window, text = "File path: " + file_path).pack()
    print(type(file_path))

def gen_summary():
    print("summary generated")
    find_summary(file_path)
    os.remove('interim_audio.mp3')
    os.remove('interim_audio.wav')



window = Tk()
# Creating a button to search the file
b1 = Button(window, text = "Open File", command = get_file_path).pack()
b2 = Button(window, text ="generate summary", command = gen_summary).pack()

window.mainloop()
print(file_path)