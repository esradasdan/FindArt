FROM python:3.8.8

WORKDIR /.code

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install requests

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]