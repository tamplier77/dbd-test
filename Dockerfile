FROM tamplier77/dbdtest
ADD . /app
WORKDIR /app
#RUN pip install boto3 flask

COPY ./app /app
CMD ["python", "main.py"]
