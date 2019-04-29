FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app
COPY uwsgi.ini /etc/uwsgi.ini

CMD uwsgi --ini /etc/uwsgi.ini