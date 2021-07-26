FROM python:3.8
LABEL maintainer="Nandini Proothi"
#copies the current dir into /app dir of the container
COPY . /app 
#sets /app as the working dir of the container (this is where the command is executed)
WORKDIR /app 
RUN pip install -r requirements.txt
CMD ["python", "app.py"]