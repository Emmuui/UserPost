FROM python:3.10

WORKDIR /app

COPY req.txt /app/req.txt

RUN pip install --upgrade pip
RUN pip install -r req.txt

COPY .. /app
