FROM python:3
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP hello.py
RUN mkdir /code 
WORKDIR /code
ADD requirements.txt /code
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "flask", "run" ]