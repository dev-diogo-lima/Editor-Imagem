import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import numpy as np

from utils import *

PADDING = 20

class FrameControles(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.var_nome_arquivo = tk.StringVar(value='Nome Imagem')
        self.flag_imagem = False

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure([1, 2, 3], weight=1)

        label_original = ttk.Label(self, text='Imagem Original', padding=(5, 0), style='MainText.TLabel')
        frame_pad = ttk.Frame(self, width=3, style='Espacador.TFrame')
        label_nome_imagem = ttk.Label(self, textvariable=self.var_nome_arquivo, padding=(5, 0, 5, 5), style='MainText.TLabel')
        # label_brilho = ttk.Label(self, text='Brilho:')
        # dlabel_brilho = ttk.Label(self, textvariable=self.var_brilho)
        
        frame_pad.grid(row=0, column=0, rowspan=4, sticky='nsw')
        label_original.grid(row=0, column=1, padx=20, pady=(10, 0), sticky='sw')
        label_nome_imagem.grid(row=2, column=1, padx=20, pady=(0, 10), sticky='ne')
        # label_brilho.grid(row=2, column=1, sticky='we')
        # dlabel_brilho.grid(row=3, column=1, sticky='we')
        
        self.frame_imagem_original = ttk.Frame(self, style='FrameImagens.TFrame')
        self.frame_imagem_original.grid(row=1, column=1, padx=20, pady=0, sticky='nsew')
        self.frame_imagem_original.grid_columnconfigure(0, weight=1)
        self.frame_imagem_original.grid_rowconfigure(0, weight=1)

        self.canvas_img_original = tk.Canvas(self.frame_imagem_original, highlightthickness=0)
        largura, altura = (self.frame_imagem_original.winfo_width(), self.frame_imagem_original.winfo_height())
        self.canvas_img_original.configure(background=COR_BACKGROUND_IMAGENS, height=largura, width=altura)
        self.canvas_img_original.grid(row=0, column=0, sticky='nsew')
        

        # self.label_imagem_original = ttk.Label(self.frame_imagem_original, background=COR_BACKGROUND_IMAGENS)
        # self.label_imagem_original.configure(anchor='center')
        # self.label_imagem_original.pack(fill='both', expand=True)

        self.bind('<Configure>', self._reajustar_imagem)

    def func_abrir(self, file: str):
        self.flag_imagem = True
        self.var_nome_arquivo.set(file.split('/')[-1])
        self.imagem = Image.open(file)
        self._reajustar_imagem()
        self.figura = ImageTk.PhotoImage(self.imagem)
        self.container_imagem = self.canvas_img_original.create_image((self.frame_imagem_original.winfo_width() / 2, self.frame_imagem_original.winfo_height() / 2), image=self.figura, anchor='center', tag='original')

    def _reajustar_imagem(self, *args):
        if self.flag_imagem:
            largura_frame = self.frame_imagem_original.winfo_width() - PADDING
            altura_frame = self.frame_imagem_original.winfo_height() - PADDING
            self.imagem = ImageOps.contain(image=self.imagem, size=(largura_frame, altura_frame))
            for imagem in self.canvas_img_original.find_withtag('original'):
                self.canvas_img_original.coords(imagem, (self.frame_imagem_original.winfo_width() / 2, self.frame_imagem_original.winfo_height() / 2))


if __name__ == '__main__':
    root = tk.Tk()
    
    root.geometry('400x800')
    style = ttk.Style()
    style.configure('FrameImagens.TFrame', background='black')

    frame = FrameControles(root)
    frame.pack(fill='both', expand=True)

    root.mainloop()