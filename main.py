import tkinter as tk
from HomePage import HomePage
from ViewPage import ViewPage
from SlideshowPage import SlideshowPage
import os
from config import *

# CREATE EXECUTABLE - $ pyinstaller --onefile main.py

class App(tk.Tk):
    def __init__(self):
        self.win = tk.Tk.__init__(self)

        self.title("PhotoViewer")

        self.container = tk.Frame(self)
        self.container.pack()

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = [HomePage(self.container, self), ViewPage(self.container, self), SlideshowPage(self.container, self)]
        for f in self.frames:
            f.grid(row=0, column=0, sticky="nsew")
        
        self.showFrame("HOME")
    

    def showFrame(self, ID):
        print(self.winfo_width(), self.winfo_height())
        for f in self.frames:
            if f.ID == ID:
                f.tkraise()

# make necessary directories
for d in [SIMG_DIR, SS_DIR, CAP_DIR]:
    if not os.path.exists(d):
        os.mkdir(d)
app = App()
app.mainloop()
