import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

if __name__ == '__main__':
    from scroll import FrameScroll


class FrameDisplay(FrameScroll):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.canvas.configure(height=800, width=1200)

        imagem = Image.open(r'assets\panda.png')
        self.figura = ImageTk.PhotoImage(imagem)
        self.canvas.create_image((0, 0), image=self.figura, tag='figura')

    
    def geometry(self, tuple: tuple[int, int]) -> None:
        largura, altura = tuple
        self.canvas.configure(width=largura, height=altura)


if __name__ == '__main__':   
    root = tk.Tk()
    
    sframe = FrameDisplay(root)
    sframe.pack()

    root.mainloop()