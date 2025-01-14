FROM python:3.13-bookworm

WORKDIR /app

COPY ./src /app
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
