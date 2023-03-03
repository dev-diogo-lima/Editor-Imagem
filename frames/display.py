import tkinter as tk
from tkinter import ttk

from frames.canvas import FrameCanvas

class FrameDisplay(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_canvas = FrameCanvas(self)
        self.frame_canvas.grid(row=0, column=0, sticky='nsew')

