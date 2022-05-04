FROM python:3.10.4-alpine3.15

RUN python -m pip install --upgrade pip

RUN pip install flask

RUN pip install flask_sqlalchemy

RUN pip install psycopg2-binary

RUN apk add curl

WORKDIR /app

COPY app/ /app

EXPOSE 5000

CMD ["python","atividade.py"]

