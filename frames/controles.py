import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import numpy as np

from frames.canvas import FrameCanvas

PADDING = 20

class FrameControles(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.var_nome_arquivo = tk.StringVar(value='Nome arquivo')
        self.var_contraste = tk.StringVar(value='1')

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=3)

        label_original = ttk.Label(self, text='Imagem Original', padding=(5, 0), style='MainText.TLabel')
        frame_pad = ttk.Frame(self, width=5, style='Espacador.TFrame')
        label_nome_imagem = ttk.Label(self, textvariable=self.var_nome_arquivo, padding=(5, 0, 5, 5), style='MainText.TLabel', width=20)
        label_nome_imagem.configure(anchor='center')

        frame_pad.grid(row=0, column=0, rowspan=4, sticky='nsw')
        label_original.grid(row=0, column=1, padx=20, pady=(10, 0), sticky='sw')
        label_nome_imagem.grid(row=2, column=1, padx=20, pady=(0, 10), sticky='nwe')
        
        self.canvas_imagem_original = FrameCanvas(self)
        self.canvas_imagem_original.grid(row=1, column=1, padx=20, pady=0, sticky='nsew')

        self.frame_contraste = ttk.Frame(self)
        self.frame_contraste.grid(row=3, column=1, padx=20, pady=10, sticky='nswe')
        self.frame_contraste.grid_columnconfigure(0, weight=1)

        label_contraste = ttk.Label(self.frame_contraste, text='Contraste')
        self.slider_contraste = ttk.Scale(self.frame_contraste, orient='horizontal', from_=0, to=10, command=self.alterar_contraste, variable=self.var_contraste)

        label_contraste.grid(row=0, column=0, sticky='we')
        self.slider_contraste.grid(row=1, column=0, sticky='we')


    def carregar_imagem(self, caminho_imagem):
        self.var_nome_arquivo.set(caminho_imagem.split('/')[-1])
        self.canvas_imagem_original.carregar_imagem(caminho_imagem)

    def alterar_contraste(self, event):
        
        pass


        
        

if __name__ == '__main__':
    root = tk.Tk()
    
    root.geometry('400x800')
    style = ttk.Style()
    style.configure('FrameImagens.TFrame', background='black')

    frame = FrameControles(root)
    frame.pack(fill='both', expand=True)

    root.mainloop()