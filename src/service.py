import pickle
import os

from .corrida import Corrida

model_path = os.path.join('resources', 'model')

class Service:

    def __load_model__(self):
        with open(model_path, 'rb') as file:
            return pickle.load(file)

    def execute(self, request):
        corrida = Corrida(request)
        model = self.__load_model__()

        return model.predict(corrida.get_np_array())