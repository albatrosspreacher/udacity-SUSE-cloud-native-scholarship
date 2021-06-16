FROM python:3.8
LABEL maintainer="Nandini Proothi"
COPY . 1-endpoints
WORKDIR /1-endpoints
RUN pip install -r 1-endpoints/requirements.txt
CMD ["python", "1-endpoints/app.py"]