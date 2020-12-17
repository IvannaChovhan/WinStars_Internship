FROM python:3.8.2

WORKDIR /model
COPY main.py /model
COPY requirements.txt /model

RUN pip install -r requirements.txt

ENTRYPOINT  ["python", "main.py"]