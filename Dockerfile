FROM ubuntu:latest
MAINTAINER Ivan Caceres "ivansfy@gmail.com"
RUN apt-get update -y
RUN apt-get install -y mongodb-clients
RUN apt-get install -y nmap
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]