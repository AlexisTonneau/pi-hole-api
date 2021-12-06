FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]
