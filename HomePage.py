import tkinter as tk
from tkinter import ttk
from config import *

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.ID = "HOME"

        l = ttk.Label(self, text="Home", font=LARGE_FONT)
        l.pack(pady=80)

        to_page1 = ttk.Button(self, text="View Saved Images", command=lambda:[controller.showFrame("VIEW"), self.controller.frames[1].loadCaptions()])
        to_page1.pack(pady=30)

        to_page2 = ttk.Button(self, text="Slideshow!", command=lambda:controller.showFrame("SLIDESHOW"))
        to_page2.pack(pady=30)