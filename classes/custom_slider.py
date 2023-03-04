import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
style = ttk.Style(root)

var = tk.StringVar()

linha = Image.open('./assets/linha.png')
seletor = Image.open('./assets/seletor.png')

img_linha = ImageTk.PhotoImage(linha)
img_seletor = ImageTk.PhotoImage(seletor)

style.element_create('custom.Scale.linha', 'image', img_linha)
style.element_create('custom.Scale.seletor', 'image', img_seletor)

style.layout('custom.Vertical.TScale',
             [('custom.Scale.linha', {'sticky': 'ns'}),
              ('custom.Scale.seletor', {'side': 'top', 'sticky': ''})])

style.layout('custom.Horizontal.TScale',
             [('custom.Scale.linha', {'sticky': 'we'}),
              ('custom.Scale.seletor', {'side': 'left', 'sticky': ''})])


class CustomScale(ttk.Scale):
    def __init__(self, master=None, **kw):
        kw.setdefault("orient", "vertical")
        self.variable = kw.pop('variable', tk.DoubleVar(master))
        ttk.Scale.__init__(self, master, variable=self.variable, **kw)
        self._style_name = '{}.custom.{}.TScale'.format(self, kw['orient'].capitalize()) # unique style name to handle the text
        self['style'] = self._style_name
        self.variable.trace_add('write', self._update_text)
        self._update_text()

    def _update_text(self, *args):
        style.configure(self._style_name, text="{:.1f}".format(self.variable.get()))


scale = CustomScale(root, from_=0, to=10)
scale.pack(side='left')

root.mainloop()


