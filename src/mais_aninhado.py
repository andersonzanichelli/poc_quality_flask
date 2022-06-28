class MaisAninhado:
    dado: str
    valor: float

    def __init__(self, mais_aninhado):
        self.dado = mais_aninhado['dado']
        self.valor = mais_aninhado['valor']