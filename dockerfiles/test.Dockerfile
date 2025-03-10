FROM python:3.13-bookworm

WORKDIR /app

COPY ./src /app
RUN pip install -r test-requirements.txt

ENV PYTHONPATH=/app

CMD ["pytest", "-vvv"]
