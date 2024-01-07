# FROM ubuntu:20.04
# RUN apt-get update && apt-get install -y python3.9 python3.9-dev
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# CMD ["python]

FROM python:3.8.5-slim
COPY requirements.txt /
RUN pip install -r /requirements.txt