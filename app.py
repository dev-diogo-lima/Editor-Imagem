import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from utils import *


from frames import FrameScroll, FrameFerramentas, FrameControles, FrameCanvas
from classes import Image

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Editor de Imagem')
        self.minsize(1200, 800)
        self.state('zoomed')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Main.TFrame', background=COR_BACKGROUND_PRINCIPAL)
        self.style.configure('MainText.TLabel', background=COR_BACKGROUND_IMAGENS, foreground=COR_FOREGROUND_IMAGENS, font=('Segoe UI', 10, 'bold'))
        self.style.configure('Espacador.TFrame', background=COR_ESPACADOR)

        self.style.configure('ToolBar.TFrame', background=COR_BACKGROUND_TOOLBAR)
        self.style.configure('ToolBar.TButton' ,relief='flat', background=COR_BACKGROUND_TOOLBAR, foreground=COR_FOREGROUND_TOOLBAR, font=('Segoe Ui', 10, 'bold'))
        self.style.map('ToolBar.TButton', background=[('active', COR_BOTAO_HOVER_TOOLBAR)])

        self.style.configure('Controls.TFrame', background=COR_BACKGROUND_CONTROLES)
        self.style.configure('FrameImagens.TFrame', background=COR_BACKGROUND_IMAGENS)

        self.frame_principal = ttk.Frame(self, style='Main.TFrame')
        self.frame_principal.grid(row=0, column=0, sticky='nsew')
        self.frame_principal.grid_columnconfigure(0, weight=4)
        self.frame_principal.grid_columnconfigure(1, weight=1)
        self.frame_principal.grid_rowconfigure(1, weight=1)

        self.frame_controles = FrameControles(self.frame_principal, style='Controls.TFrame')
        self.frame_controles.grid(row=1, column=1, sticky='nwse')

        self.frame_imagem = FrameCanvas(self.frame_principal, style='FrameImagens.TFrame')
        self.frame_imagem.grid(row=1, column=0, sticky='nswe', padx=50, pady=50)

        self.frame_ferramentas = FrameFerramentas(self.frame_principal, self.frame_controles.func_abrir, self.frame_imagem.salvar_imagem, self.frame_imagem.carregar_imagem, style='ToolBar.TFrame')
        self.frame_ferramentas.grid(row=0, column=0, columnspan=2, sticky='nwe')

        # label = ttk.Label(self.frame_principal, text='Place Holder')
        # label.grid(row=1, column=0, sticky='we')
        

        # self.frame_display = ttk.Frame(self, style='Bg.TFrame')
        # self.frame_display.grid(row=0, column=0, sticky='nsew')
        # self.frame_display.grid_columnconfigure(0, weight=1)
        # self.frame_display.grid_rowconfigure(0, weight=1)

        # self.sframe_display = FrameScroll(self.frame_display)
        # self.sframe_display.grid(row=0, column=0, sticky='nsew')

        # imagem = Image.open(r'assets\panda.png').resize((800, 600))
        # self.figura = ImageTk.PhotoImage(imagem)
        # self.sframe_display.canvas.create_image((0, 0), image=self.figura, tag='panda')
        


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
