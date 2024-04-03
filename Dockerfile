FROM python:3.11-alpine

RUN mkdir '/parse_posts'

WORKDIR /parse_posts

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .