# Dockerfile
FROM python:3.8-slim

ENV API_KEY="12345-abcde-67890-fghij"
ENV DB_PASSWORD="sup3rS3cr3t!"

COPY . /app
WORKDIR /app
RUN --mount=type=secret,id=mytoken TOKEN=$(cat /run/dooku-secrets/password)
RUN pip install -r requirements.txt

CMD ["python", "app.py"]