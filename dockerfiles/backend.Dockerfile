FROM python:3.13-bookworm

WORKDIR /app

COPY ./src /app

CMD ["python", "main.py"]
