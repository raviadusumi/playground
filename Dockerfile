FROM python:3

WORKDIR /workdir

COPY requirements.txt ./
COPY ./ /workdir

RUN pip install --no-cache-dir -r requirements.txt
