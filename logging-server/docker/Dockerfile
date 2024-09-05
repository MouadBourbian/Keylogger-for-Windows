FROM python:3.9-slim

WORKDIR /app
COPY log_server.py /app/log_server.py
RUN pip install flask

EXPOSE 5000

CMD ["python", "log_server.py"]