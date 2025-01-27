FROM python:3.10

ENV PYTHONBUFFERD=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn TSharma.wsgi:application"]