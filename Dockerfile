FROM python:3-stretch

ADD ./app/ /app

RUN cd /app && \
    pip install -r requirements.txt

WORKDIR /app

RUN ["python", "run.py"]