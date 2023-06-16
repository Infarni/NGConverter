FROM python:3.11-alpine
LABEL authors="archdrdr"

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "main.py"]

COPY . /app

EXPOSE 8000
