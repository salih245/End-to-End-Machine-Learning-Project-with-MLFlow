FROM python:3.10-slim-bullseye

RUN apt-get update -y && apt-get install -y awscli

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]