#Import the required library
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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

trough = Image.open('./assets/linha.png')
slider = Image.open('./assets/seletor.png')

root = tk.Tk()
# create images used for the theme (instead of using the data option, it is 
# also possible to use .gif or .png files)
img_trough = ImageTk.PhotoImage(trough)
img_slider = ImageTk.PhotoImage(slider)
style = ttk.Style(root)
# create scale elements
style.element_create('custom.Scale.trough', 'image', img_trough)
style.element_create('custom.Scale.slider', 'image', img_slider)
# create custom layout
style.layout('custom.Vertical.TScale',
             [('custom.Scale.trough', {'sticky': 'ns'}),
              ('custom.Scale.slider',
               {'side': 'top', 'sticky': '',
                'children': [('custom.Vertical.Scale.label', {'sticky': 'we'})]
                })])

scale1 = CustomScale(root, from_=0, to=10)
scale1.pack(side='left')
scale2 = CustomScale(root, from_=0, to=100)
scale2.pack(side='left')
root.mainloop()