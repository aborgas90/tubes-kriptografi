FROM python:3.8-alpine

ENV PYTHONUNBUFFERED True

# Set WORKDIR ke dalam direktori /app
WORKDIR /app

# Salin seluruh konten dari direktori proyek ke dalam WORKDIR
COPY . .

# Install dependensi Python
RUN pip install -r requirements.txt

# Atur perintah default untuk menjalankan aplikasi
CMD ["gunicorn", "--bind", ":5000", "--workers", "1", "--threads", "8", "--timeout", "0", "app:app"]