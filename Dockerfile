FROM mcr.microsoft.com/playwright/python:v1.64.1

WORKDIR /app

COPY . .

RUN ["pip", "install", "--no-cache-dir", "-r", "requirements.txt"]

CMD ["pytest"]
