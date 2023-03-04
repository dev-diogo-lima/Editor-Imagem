import tkinter as tk
from tkinter import ttk
from utils import *

from PIL import Image, ImageOps

from classes import Imagem

class FrameCanvas(ttk.Frame):
    def __init__(self, container: ttk.Frame, *args, root=None, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.canvas = tk.Canvas(self, highlightthickness=0, borderwidth=0, background=COR_BACKGROUND_IMAGENS)
        self.canvas.place(x=0, y=0)

    def carregar_imagem(self, caminho_imagem: str):
        self.ajuste_tamanho()
        self.imagem = Imagem(caminho_imagem)
        self.imagem.ajuste_tamanho(self.canvas.winfo_width(), self.canvas.winfo_height(), 20)
        self.objeto = self.canvas.create_image((self.winfo_width() / 2, self.winfo_height() / 2), image=self.imagem.get_figura(), anchor='center', tag='imagem')
        return self.objeto


    def salvar_imagem(self, nome_arquivo=None):
        self.imagem.export(nome_arquivo)

    def ajuste_tamanho(self, *args):
        self.canvas.configure(width=self.winfo_width(), height=self.winfo_height())
        

if __name__ == '__main__':
    root = tk.Tk()
    style = ttk.Style()
    style.configure('Teste.TFrame', background='#10141f')
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    frame = FrameCanvas(root, style='Teste.TFrame')
    frame.canvas.config(background='#c7cfcc')
    frame.grid(row=0, column=0, sticky='nsew')

    root.mainloop()