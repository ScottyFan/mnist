FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

RUN mkdir -p /app/data

CMD ["python", "main.py", "--epochs", "5", "--batch-size", "128", "--lr", "0.5"]