FROM python:3.9-slim-buster

ENV MYSQL_DATABASE=bse
ENV MYSQL_ROOT_PASSWORD=

RUN apt-get update && apt-get install -y mariadb-server mariadb-client

COPY ./bulk_deals.sql /docker-entrypoint-initdb.d/
COPY ./requirements.txt /app/
RUN /etc/init.d/mysql start && \
    mysql -u root -p$MYSQL_ROOT_PASSWORD < /docker-entrypoint-initdb.d/bulk_deals.sql

RUN pip install -r /app/requirements.txt

COPY ./scrapper.py /app/
COPY ./* /app/
WORKDIR /app

EXPOSE 8000

CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & while true; do python scrapper.py; sleep 86400; done"]
