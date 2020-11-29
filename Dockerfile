FROM python:3.8-slim-buster

WORKDIR /app
COPY app.py .
COPY requirements.txt .

RUN apt -y update && apt-get -y build-dep python3-lxml
RUN pip install -r requirements.txt


ENTRYPOINT ["python", "app.py"]