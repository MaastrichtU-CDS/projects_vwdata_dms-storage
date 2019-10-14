FROM python:3-stretch

ADD ./app/ /app

RUN cd /app && \
    pip install -r requirements.txt

WORKDIR /app

CMD ["python", "run.py"]