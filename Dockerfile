FROM python:3.11

ENV DockerHOME=/home/app/webapp

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHOME
RUN rm $DockerHOME/db.sqlite3

RUN pip install -r requirements.txt

EXPOSE 8000

RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000