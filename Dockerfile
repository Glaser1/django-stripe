FROM python:3.10-slim

RUN mkdir /app

COPY . /app

 
RUN pip3 install -r /app/requirements.txt --no-cache-dir

WORKDIR /app/stripe_payment

CMD ["python3", "manage.py", "runserver", "0:8000"] 
