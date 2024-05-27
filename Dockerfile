FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

# Set WORKDIR ke dalam direktori /app
WORKDIR /app

# Salin seluruh konten dari direktori proyek ke dalam WORKDIR
COPY . .

# Install dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Atur perintah default untuk menjalankan aplikasi
CMD ["gunicorn", "--bind", ":5000", "--workers", "1", "--threads", "8", "--timeout", "0", "main:app"]