import numpy as np

from .aninhado import Aninhado

class Corrida:
    def __init__(self, request):
        self.sepal_length = float(request['sepal_length'])
        self.sepal_width = float(request['sepal_width'])
        self.petal_length = float(request['petal_length'])
        self.petal_width = float(request['petal_width'])
        self.aninhado = Aninhado(request['aninhado'])

    def get_np_array(self):
        return np.array([[
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width]])

    @staticmethod
    def get_schema():
        return {
            "type": "object",
            "properties": {
                "sepal_length": { "type": "number" },
                "sepal_width": { "type": "number" },
                "petal_length": { "type": "number" },
                "petal_width": { "type": "number" },
                "aninhado": {
                    "type": "object",
                    "properties": {
                        "exemplo": {"type": "string"},
                        "mais_aninhado": {
                            "type": "object",
                            "properties": {
                                "dado": {"type": "string"},
                                "valor": {"type": "number"}
                            }
                        }
                    }
                }
            },
            "required": ["sepal_length", "sepal_width", "petal_length", "petal_width", "aninhado"]
        }

    def __str__(self):
        return f"""{ 
            "sepal.length": self.sepal_length
            }"""