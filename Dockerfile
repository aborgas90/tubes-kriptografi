FROM python:alpine3.7
COPY requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt
COPY app.py .
CMD ["gunicorn", "--bind", ":5000", "--workers", "1", "--threads", "8", "--timeout", "0", "main:app"]