import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from pathlib import Path

class FrameFerramentas(ttk.Frame):
    def __init__(self, container, func_abrir, func_salvar, func_carregar_imagem, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.func_abrir = [func_abrir, func_carregar_imagem]
        self.func_salvar = func_salvar
        self.grid_columnconfigure(2, weight=1)

        botao_abrir = ttk.Button(self, text='Abrir', command=self._comando_abrir, style='ToolBar.TButton', padding=0)
        botao_abrir.grid(row=0, column=0, sticky='we', padx=2, pady=(2, 0), ipady=2, ipadx=2)

        botao_salvar = ttk.Button(self, text='Salvar', command=self._comando_salvar, style='ToolBar.TButton', padding=0)
        botao_salvar.grid(row=0, column=1, sticky='we', padx=2, pady=(2, 0), ipady=2, ipadx=2)

        frame_pad = ttk.Frame(self, height=3, style='Espacador.TFrame')
        frame_pad.grid(row=1, column=0, sticky='we', columnspan=3)

    def _comando_abrir(self):
        file = fd.askopenfile(title='Selecione a Imagem', initialdir=Path.cwd())
        self.func_abrir[0](file.name)
        self.func_abrir[1](file.name)

    def _comando_salvar(self):
        self.func_salvar()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('600x400')
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('ToolBar.TButton', relief='flat')

    root.grid_columnconfigure(0, weight=1)

    frame = FrameFerramentas(root)
    frame.grid(row=0, column=0, sticky='we')

    root.mainloop()