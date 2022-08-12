FROM python:3.7-slim-buster

ADD . /app
WORKDIR /app

COPY wait-for-it.sh wait-for-it.sh 
RUN chmod +x wait-for-it.sh

# Install python packages
RUN pip install mlflow boto3 pymysql minio sklearn
COPY train.py train.py
COPY kc_house_data.csv kc_house_data.csv
ENTRYPOINT ./wait-for-it.sh db:3306 -t 90 -- mlflow server --backend-store-uri mysql+pymysql://mlflow_user:mlflow_password@db:3306/mlflow --default-artifact-root s3://ml-flowbucket/ -h 0.0.0.0

