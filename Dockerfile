FROM python:3.5-alpine
ADD . /app
WORKDIR /app
RUN pip install boto3 flask

COPY ./app /app
CMD ["python", "main.py"]
