FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir "flask>=3.1.1" "flask-mail>=0.10.0" "gunicorn>=23.0.0" "python-dotenv>=1.1.1"

COPY . .

ENV PORT=5000
EXPOSE 5000

CMD ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:${PORT}"]
