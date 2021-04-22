FROM python:3.7.3-stretch
WORKDIR /app
ADD . /app
RUN pip install -r requirement.txt
CMD ["uwsgi","cconfig.ini"]
