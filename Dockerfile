FROM python:3.9.0

WORKDIR /home/

RUN echo 'asdhasdh'

RUN git clone https://github.com/horry77/gjs4.git

WORKDIR /home/gjs4/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=gjs4.settings.deploy && python manage.py migrate --settings=gjs4.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gjs4.settings.deploy gjs4.wsgi --bind 0.0.0.0:8500"]





