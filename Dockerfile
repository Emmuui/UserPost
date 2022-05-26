FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app

RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media

WORKDIR $APP_HOME

COPY req.txt /home/app/web/

RUN pip install --upgrade pip
RUN pip install -r /home/app/web/

COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

# change to the app user
USER app

