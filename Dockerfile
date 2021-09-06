FROM ubuntu:latest
RUN apt-get -y  update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
COPY ./requirements.txt /flask_app/requirements.txt
WORKDIR /flask_app
RUN pip3 install -r requirements.txt
COPY . /flask_app
ENTRYPOINT ["python3"]
CMD ["flask_api.py"]
