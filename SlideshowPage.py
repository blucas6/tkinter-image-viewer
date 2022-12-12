import tkinter as tk
from tkinter import StringVar, ttk
import random as rand
from PIL import Image, ImageTk
import os

from config import *
from ImageDisplayer import *

class SlideshowPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.ID = "SLIDESHOW"

        self.TIMER = StringVar(value=4) 

        # TITLE
        l = ttk.Label(self, text="Slideshow")
        l.grid(row=0, column=2, pady=20)

        # Back Button
        BACK = ttk.Button(self, text="Back to Home", command=lambda:[controller.showFrame("HOME"), self.endSlideShow()])
        BACK.grid(row=12, column=0, pady=20)

        # Canvas 
        self.CANVAS = tk.Canvas(self, width=CANVAS_W, height=CANVAS_H, bd=5, relief="raised")
        self.CANVAS.grid(row=1, column=0, rowspan=10, columnspan=5, padx=5)

        # Images
        self.IMG_LIST = []
        self.IMG_LIST = IM_loadImageList(SS_DIR)
        if len(self.IMG_LIST) > 1:
            self.INDEX = rand.randint(0, len(self.IMG_LIST)-1)
        else:
            self.INDEX = 0

        # start slideshow
        self.SS_on = False
        start_b = ttk.Button(self, text="Start Slideshow", command=lambda:[self.loadImageList(), self.startSlideshow()])
        start_b.grid(row=0, column=4)

        # stop slideshow
        stop_b = ttk.Button(self, text="Stop Slideshow", command=lambda:self.endSlideShow())
        stop_b.grid(row=0, column=0)

        # time spinbox
        timer_s = ttk.Spinbox(self, from_=1, to=20, textvariable=self.TIMER)
        timer_s.grid(row=0, column=3)

    def nextImage(self):
        print(self.INDEX, len(self.IMG_LIST), self.TIMER.get())
        if len(self.IMG_LIST) == 0:
            self.SS_on = False
        elif self.SS_on:
            IM_viewImage(SS_DIR, self.CANVAS, self.IMG_LIST, self.INDEX)
            self.IMG_LIST.remove(self.IMG_LIST[self.INDEX])
            if len(self.IMG_LIST) <= 1:
                self.INDEX = 0
            else:
                self.INDEX = rand.randint(0, len(self.IMG_LIST)-1)
            if self.SS_on:
                self.CANVAS.after(int(self.TIMER.get())*1000, lambda:self.nextImage())

    def startSlideshow(self):
        if not self.SS_on:
            self.SS_on = True
            self.nextImage()
    
    def endSlideShow(self):
        self.SS_on = False

    def loadImageList(self):
        self.IMG_LIST = IM_loadImageList(SS_DIR)
