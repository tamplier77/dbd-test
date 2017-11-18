FROM tiangolo/uwsgi-nginx-flask:python3.5

RUN pip install boto3

COPY ./app /app
#COPY ./nginx.conf /etc/nginx/conf.d/
