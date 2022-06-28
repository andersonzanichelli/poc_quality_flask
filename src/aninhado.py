from .mais_aninhado import MaisAninhado

class Aninhado:
    exemplo: str
    maisaninhado: MaisAninhado

    def __init__(self, aninhado):
        self.exemplo = aninhado['exemplo']
        self.maisaninhado = aninhado['mais_aninhado']