# POC Quality com Flask API

Nessa poc utilizaremos o framework Flask API para avaliação de desempenho.


## Para executar a aplicação localmente:
Crie um environment python antes pe executar os próximos passos!
```
$ pip install -r requirements.txt
$ set FLASK_APP=main.py
$ flask run
```

## Para gerar uma imagem docker
```
$ docker build --tag poc-quality-flask .
$ docker run -p 5000:5000 poc-quality-flask:latest
```