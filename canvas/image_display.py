import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import numpy as np

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

    def carregar_imagem(self, path):
        self.setup(path)
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
        array_parcial = 255 / (maximo - minimo) * (array_parcial - minimo)
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

if __name__ == '__main__':
    root = tk.Tk()
    style = ttk.Style(root)

    style.theme_use('clam')

    canvas = CanvasDinamico(root, background='red')
    canvas.carregar_imagem('./assets/panda.png')
    canvas.atualizar_imagem()
    canvas.pack()     

    botao_carregar = ttk.Button(root, text='carregar', command=lambda: canvas.carregar_imagem('./assets/panda.png'))
    botao_carregar.pack()
    botao_atualizar = ttk.Button(root, text='Reset', command=canvas.reset)
    botao_atualizar.pack()
    slider_brilho = tk.Scale(root, orient='horizontal', from_=-255, to=255, variable=canvas.val_brilho, digits=1, command=canvas.atualizar_imagem, resolution=2, showvalue=False)
    slider_brilho.pack()
    # slider_contraste_min = ttk.Scale(root, orient='horizontal', from_=0, to=255, variable=canvas.val_contraste_min, command=canvas.atualizar_imagem)
    # slider_contraste_min.pack()
    # slider_contraste_max = ttk.Scale(root, orient='horizontal', from_=0, to=255, variable=canvas.val_contraste_max, command=canvas.atualizar_imagem)
    # slider_contraste_max.pack()


    root.mainloop()
        
