import tkinter as tk
from tkinter import ttk

class FrameScroll(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure([0, 1], weight=0)

        # Criando Canvas
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # Criando Scroll Vertical
        self.scroll_vertical = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scroll_vertical.grid(row=0, column=1, sticky='ns')

        # Criando Scroll Horizontal
        self.scroll_horizontal = ttk.Scrollbar(self, orient='horizontal', command=self.canvas.xview)
        self.scroll_horizontal.grid(row=1, column=0, sticky='we')

        # Configurando Canvas
        self.canvas.configure(yscrollcommand=self.scroll_vertical.set, xscrollcommand=self.scroll_horizontal.set)
        self.canvas.bind('<Configure>', lambda event: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        # Frame Secundário
        self.frame = ttk.Frame(self.canvas, *args, **kwargs)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

if __name__ == '__main__':
    root = tk.Tk()

    frame_scroll = FrameScroll(root)
    frame_scroll.pack(fill='both', expand=True)

    label = ttk.Label(frame_scroll.frame, text='aa' * 200)
    label.pack()


    root.mainloop()