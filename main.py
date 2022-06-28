import logging
from logging.config import dictConfig
from flask import Flask, request
from flask_expects_json import expects_json

from src.service import Service
from src.corrida import Corrida

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

species = { 0: "Iris setosa", 1: "Iris versicolor", 2: "Iris virginica" }

logging.getLogger("mylogger")

app = Flask(__name__)

@app.post("/predict")
@expects_json(Corrida.get_schema())
def predict():
    logging.info(f'Requisicao recebida: {request.json}')

    result = Service().execute(request.json)

    resp = {
            "predição": str(result),
            "espécie": species[result[0]]
            }

    logging.info(f'Response with prediction: {resp}')

    return resp