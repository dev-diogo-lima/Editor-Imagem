# pyinstaller canvas/image_display.py --onefile, --windowed

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import numpy as np
from tkinter import filedialog as fd

class CanvasDinamico(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, highlightthickness=0, **kwargs)

        self.referencia_imagem = None
        self.val_brilho = tk.StringVar(value='0')
        self.val_contraste_min = tk.StringVar(value='0')
        self.val_contraste_max = tk.StringVar(value='255')

    def _correcao_modo(self):
        if self.imagem_original.mode == 'I':
            array_32 = np.array(self.imagem_original)
            array_8 = np.right_shift(array_32, 8).astype(np.uint8)
            self.imagem_original = Image.fromarray(array_8)

    def carregar_imagem(self):
        arquivo = fd.askopenfilename()
        self.setup(arquivo)
        self.atualizar_imagem()

    def setup(self, path):
        self.imagem_original = Image.open(path)
        self._correcao_modo()
        self.array_imagem = np.array(self.imagem_original, dtype=np.uint8)
        self.figura = ImageTk.PhotoImage(self.imagem_original)
        x = self.winfo_width() // 2
        y = self.winfo_height() // 2
        self.referencia_imagem = self.create_image((x, y), image=self.figura, anchor='center', tag='imagem')

    def brilho(self, fator: tk.StringVar):
        brilho = int(fator.get())
        array_parcial = self.array_imagem.astype(np.uint16)
        array_parcial = array_parcial + brilho
        array_parcial = np.clip(array_parcial, a_min=0, a_max=255)
        self.array_imagem = array_parcial.astype(np.uint8)
         
    def preto_e_branco(self):
        imagem_parcial = Image.fromarray(self.array_imagem)
        imagem_parcial = ImageOps.grayscale(image=imagem_parcial)
        array_parcial = np.array(imagem_parcial)
        self.array_imagem = array_parcial

    def contraste(self, min: tk.StringVar, max: tk.StringVar):
        minimo , maximo = int(min.get()), int(max.get())
        array_parcial = self.array_imagem.astype(np.int16)
        array_parcial = np.divide(255, (maximo - minimo)) * (array_parcial - minimo)
        array_parcial = np.clip(array_parcial, a_min=0, a_max=255)
        self.array_imagem = array_parcial.astype(np.uint8)

    def atualizar_imagem(self, *event):
        self.array_imagem = np.array(self.imagem_original)
        self.preto_e_branco()
        self.brilho(self.val_brilho)
        self.contraste(self.val_contraste_min, self.val_contraste_max)
        self.imagem_atual = Image.fromarray(self.array_imagem)
        largura = self.winfo_width()
        altura = self.winfo_height()
        self.imagem_atual = ImageOps.contain(self.imagem_atual, size=(largura, altura))
        self.figura = ImageTk.PhotoImage(self.imagem_atual)
        self.itemconfig(self.referencia_imagem, image=self.figura)

    def reset(self):
        self.val_brilho.set('0')
        self.val_contraste_min.set('0')
        self.val_contraste_max.set('255')
        self.atualizar_imagem()

    def export(self):
        file = fd.asksaveasfile()
        imagem_export = Image.fromarray(self.array_imagem)
        imagem_export.save(file.name)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('600x400')
    root.minsize(600, 400)
    root.title('Editor Foto (Beta)')
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure('ToolBar.TButton', relief='flat')

    root.grid_columnconfigure(0, weight=1)
    # root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    canvas = CanvasDinamico(root)
    canvas.grid(row=1, column=0, sticky='nswe', pady=(5, 0))
    

    frame_sliders = ttk.Frame(root)   
    frame_sliders.grid(row=2, column=0, columnspan=3, sticky='we', padx=5)
    frame_sliders.grid_columnconfigure(0, weight=1)


    frame_toolbar = ttk.Frame(root)
    frame_toolbar.grid(row=0, column=0, sticky='we')
    # frame_toolbar.grid_columnconfigure(0, weight=1)
    botao_carregar = ttk.Button(frame_toolbar, text='Load', command=canvas.carregar_imagem, padding=0)
    botao_carregar.grid(row=0, column=0, pady=5)
    botao_atualizar = ttk.Button(frame_toolbar, text='Reset', command=canvas.reset, padding=0)
    botao_atualizar.grid(row=0, column=1, pady=5)
    botao_export = ttk.Button(frame_toolbar, text='Export', command=canvas.export, padding=0)
    botao_export.grid(row=0, column=2, pady=5)

    for botao in frame_toolbar.winfo_children():
        botao.configure(style='ToolBar.TButton')
        botao.grid_configure(sticky='w')

    slider_brilho = tk.Scale(frame_sliders, orient='horizontal', from_=-255, to=255, variable=canvas.val_brilho, digits=1, command=canvas.atualizar_imagem, resolution=2, showvalue=False, label='Brightness')
    slider_brilho.grid(row=0, column=0, sticky='we')
    slider_contraste_min = tk.Scale(frame_sliders, orient='horizontal', from_=0, to=255, variable=canvas.val_contraste_min, digits=1, command=canvas.atualizar_imagem, resolution=2, showvalue=False, label='Contrast (max)')
    slider_contraste_min.grid(row=1, column=0, sticky='we')
    slider_contraste_max = tk.Scale(frame_sliders, orient='horizontal', from_=1, to=255, variable=canvas.val_contraste_max, digits=1, command=canvas.atualizar_imagem, resolution=2, showvalue=False, label='Contrast (min)')
    slider_contraste_max.grid(row=2, column=0, sticky='we')


    root.mainloop()
        
