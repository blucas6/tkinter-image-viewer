import tkinter as tk
from tkinter import END, ttk
import os
from tkinter import filedialog
from PIL import ImageTk, Image
import random as rand
from playsound import playsound
from config import *
from ImageDisplayer import *
import shutil

class ViewPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.ID = "VIEW"

        # TITLE
        l = ttk.Label(self, text="Saved Images")
        l.grid(row=0, column=2, pady=20)

        # Play button
        play_button = ttk.Button(self, text="Play Song", command=self.play)
        play_button.grid(row=0, column=5)

        add_song = ttk.Button(self, text="Add Song", command=self.addsound)
        add_song.grid(row=0, column=6)

        # Back Button
        BACK = ttk.Button(self, text="Back to Home", command=lambda:[controller.showFrame("HOME"), self.hideCaptions()])
        BACK.grid(row=11, column=0, pady=20)

        # Canvas 
        self.CANVAS = tk.Canvas(self, width=CANVAS_W, height=CANVAS_H, bd=5, relief="raised")
        self.CANVAS.grid(row=1, column=0, rowspan=10, columnspan=5)

        # Caption list
        self.TEXT_LIST = []

        # Images
        self.IMG_LIST = []
        self.IMG_LIST = IM_loadImageList(SIMG_DIR)
        if len(self.IMG_LIST) > 1:
            self.INDEX = rand.randint(0, len(self.IMG_LIST)-1)
        else:
            self.INDEX = 0
        IM_viewImage(SIMG_DIR, self.CANVAS, self.IMG_LIST, self.INDEX)

        # Scroll images
        right_b = ttk.Button(self, text="->", command=lambda:[self.moveIndex(1), IM_viewImage(SIMG_DIR, self.CANVAS, self.IMG_LIST, self.INDEX), self.loadCaptions()])
        right_b.grid(row=0, column=3)
        left_b = ttk.Button(self, text="<-", command=lambda:[self.moveIndex(-1), IM_viewImage(SIMG_DIR, self.CANVAS, self.IMG_LIST, self.INDEX), self.loadCaptions()])
        left_b.grid(row=0, column=1)

        # Add caption button
        addcaption_b = ttk.Button(self, text="Add Caption", command=lambda:self.createCaption())
        addcaption_b.grid(row=0, column=4)

        # Save caption button
        savecaption_b = ttk.Button(self, text="Save Caption", command=lambda:[self.saveCaptions()])
        savecaption_b.grid(row=0, column=0)

    def addsound(self):
        file = filedialog.askopenfile()
        shortname = file.name.split("/").pop()
        path = SOUND_DIR+'\\'+self.IMG_LIST[self.INDEX]+'.mp3'
        if file:
            print(file.name, SOUND_DIR, shortname)
            shutil.copy(file.name, SOUND_DIR)
            os.rename(SOUND_DIR+'\\'+shortname, SOUND_DIR+'\\'+self.IMG_LIST[self.INDEX]+'.mp3')

    def play(self):
        path = f'SavedImages/Sounds/{self.IMG_LIST[self.INDEX]}.mp3'
        if os.path.exists(path):
            playsound(path)

    def saveCaptions(self):
        if self.IMG_LIST:
            c = ""
            for t in self.TEXT_LIST:
                c += t.get("1.0", END)

            with open("SavedImages/Captions/"+self.IMG_LIST[self.INDEX]+".txt", 'w+') as f:
                f.write(c)
            f.close()

    def createCaption(self, text=""):
        t = tk.Text(self, width=30, height=5)
        t.grid(row=1+len(self.TEXT_LIST), column=5)
        if text != "":
            t.insert(tk.END, text)
        self.TEXT_LIST.append(t)

    def moveIndex(self, x):
        if self.INDEX + x < 0:
            self.INDEX = len(self.IMG_LIST)-1
        elif self.INDEX + x == len(self.IMG_LIST):
            self.INDEX = 0
        else:
            self.INDEX += x

    def hideCaptions(self):
        for t in self.TEXT_LIST:
            t.destroy()

    def loadCaptions(self):
        if self.IMG_LIST:
            for t in self.TEXT_LIST:
                t.destroy()
            self.TEXT_LIST = []
            ptf = "SavedImages/Captions/"+self.IMG_LIST[self.INDEX]+".txt"
            if os.path.exists(ptf):
                f = open(ptf, 'r')
                captions = f.read()
                listc = captions.split("\n")
                for c in listc:
                    self.createCaption(c)
