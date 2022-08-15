FROM python:3.9.13-alpine3.16

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

WORKDIR /app

COPY . /app

CMD ["python", "flaskapp.py"]
