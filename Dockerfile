FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

ARG HEALTH_STATUS=200
ENV HEALTH_STATUS=${HEALTH_STATUS}
EXPOSE 8080
CMD ["python", "app.py"]
