FROM python:3.11-slim

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["python", "-m", "http.server", "5000"]