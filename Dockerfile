FROM python:3.9

ENV VIRTUAL_ENV=/opt/flaskvenv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP=/app/main

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv $VIRTUAL_ENV
RUN pip3 install -r requirements.txt
RUN mkdir src
RUN mkdir resources

COPY main.py .
COPY src ./src
COPY resources ./resources

CMD ["flask", "run", "--host", "0.0.0.0"]