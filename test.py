import tkinter as tk
import tkinter.font as tkFont
from tkinter import HORIZONTAL, INSERT, filedialog
from controller import find_summary
import os
from tkinter import Label
from tkinter import ttk

class App:

	def __init__(self, root):
		#setting title
		root.title("summary")
		#setting window size
		width=600
		height=500
		screenwidth = root.winfo_screenwidth()
		screenheight = root.winfo_screenheight()
		alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
		root.geometry(alignstr)
		root.resizable(width=False, height=False)

		GButton_341=tk.Button(root)
		GButton_341["anchor"] = "center"
		GButton_341["bg"] = "#5fb878"
		ft = tkFont.Font(family='Times',size=10)
		GButton_341["font"] = ft
		GButton_341["fg"] = "#f7f2f2"
		GButton_341["justify"] = "center"
		GButton_341["text"] = "Generate Summary"
		GButton_341.place(x=240,y=450,width=119,height=41)
		GButton_341["command"] = self.GButton_341_command

		GMessage_538=tk.Message(root)
		GMessage_538["anchor"] = "center"
		ft = tkFont.Font(family='Times',size=13)
		GMessage_538["font"] = ft
		GMessage_538["fg"] = "#333333"
		GMessage_538["justify"] = "center"
		GMessage_538["text"] = "Video Summary Generator"
		GMessage_538.place(x=120,y=10,width=356,height=56)

		self.GListBox_667=tk.Text(root)
		self.GListBox_667["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.GListBox_667["font"] = ft
		self.GListBox_667["fg"] = "#333333"
		# GListBox_667["justify"] = "center"
		self.GListBox_667.place(x=30,y=120,width=540,height=292)
		self.GListBox_667.insert(1.0,"Summary will be displayed here")


		GButton_175=tk.Button(root)
		GButton_175["bg"] = "#efefef"
		ft = tkFont.Font(family='Times',size=10)
		GButton_175["font"] = ft
		GButton_175["fg"] = "#000000"
		GButton_175["justify"] = "center"
		GButton_175["text"] = "Open File"
		GButton_175.place(x=310,y=70,width=70,height=25)
		GButton_175["command"] = self.GButton_175_command

		GMessage_124=tk.Message(root)
		ft = tkFont.Font(family='Times',size=10)
		GMessage_124["font"] = ft
		GMessage_124["fg"] = "#333333"
		GMessage_124["justify"] = "center"
		GMessage_124["text"] = "Browse File "
		GMessage_124.place(x=210,y=70,width=80,height=25)

		#Progressbar
		self.my_progress = ttk.Progressbar(root, orient=HORIZONTAL,length=300,mode="determinate")
		self.my_progress['value'] = 0
		self.my_progress.place(x=150,y=420)

	def GButton_341_command(self):
		print("Generate summary button")
		self.gen_summary()


	def GButton_175_command(self):
		print("Open File Button")
		self.get_file_path()


	def get_file_path(self):
		global file_path
		# Open and return file path
		file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
		l1 = Label(root, text = "File path: " + file_path).place(x=30,y=95)
		self.GListBox_667.delete(1.0,"end")
		self.GListBox_667.insert(INSERT,"Now click on generate summary")
		print(type(file_path))
		self.my_progress['value']=20

	def gen_summary(self):
		result=find_summary(self,file_path)
		os.remove('interim_audio.mp3')
		os.remove('interim_audio.wav')
		self.GListBox_667.delete(1.0,"end")
		self.GListBox_667.insert(1.0,result)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
