from PIL import Image, ImageOps, ImageEnhance, ImageTk
import numpy as np
from pathlib import Path
import time

class Imagem:
    def __init__(self, path_imagem):
        self.imagem = Image.open(path_imagem)
        self.imagem = self.imagem.convert('RGB')
        self.nome_imagem = path_imagem.split('/')[-1]

    def brilho(self, qtde):
        array_imagem = np.array(self.imagem, dtype=np.uint16)
        array_imagem = array_imagem + qtde
        array_imagem = np.clip(array_imagem, a_min=0, a_max=255)
        self.imagem = Image.fromarray(array_imagem.astype(np.uint8), mode='RGB')

    def preto_e_branco(self):
        self.imagem = ImageOps.grayscale(self.imagem)

    def contraste(self, min, max):
        imagem_pb = ImageOps.grayscale(self.imagem)
        array_imagem = np.array(imagem_pb).astype(np.int16)
        array_imagem = 255 / (max - min) * (array_imagem - min)
        array_imagem = np.clip(array_imagem, a_min=0, a_max=255)
        self.imagem = Image.fromarray(array_imagem.astype(np.uint8))
    
    def rotacao(self, graus, fill='black'):
        self.imagem = self.imagem.rotate(graus, expand=True, fillcolor=fill)

    def export(self, novo_nome=None):
        pasta_output = Path.cwd() / 'output'
        pasta_output.mkdir(exist_ok=True)

        if not novo_nome:
            lista_nomes = self.nome_imagem.split('.')
            novo_nome = f'{int(time.time())}.'.join(lista_nomes)

        self.imagem.save(pasta_output / novo_nome)
        return None

    def get_figura(self):
        self.figura = ImageTk.PhotoImage(self.imagem)
        return self.figura

    
if __name__ == '__main__':
    img = Imagem('./assets/G1 Ponto2_300mT_2.png')
    array = np.array(img.imagem)
    print(np.amax(array), np.amin(array))
    # img.brilho(30)
    # img.preto_e_branco()
    img.contraste(60, 170)
    img.export()
    # img.rotacao(-87)
