FROM python:3.7-slim

RUN python -m pip install --upgrade pip

RUN pip install pandas

RUN pip install flask

RUN pip install flask_sqlalchemy

RUN pip install psycopg2-binary

WORKDIR /app

COPY app/ /app

EXPOSE 5000

CMD ["python","atividade.py"]

