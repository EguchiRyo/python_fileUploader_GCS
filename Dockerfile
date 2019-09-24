FROM python:3
RUN pip install google-cloud-storage

ADD . /root
EXPOSE 80