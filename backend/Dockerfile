FROM python:3.8-slim
WORKDIR /app
COPY app.py /app
RUN pip install flask psycopg2-binary
CMD ["python", "app.py"]