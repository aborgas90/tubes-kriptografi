# Gunakan image dasar Python
FROM python:3.9-slim

# Setel variabel lingkungan untuk memastikan Python tidak membuat file cache .pyc
ENV PYTHONUNBUFFERED True

# Tentukan direktori kerja di dalam container
ENV APP_HOME /app
WORKDIR $APP_HOME

# Salin file requirements.txt ke direktori kerja
# COPY requirements.txt .
COPY . ./
# Instal dependensi Python
RUN pip install -r requirements.txt

# Salin semua kode ke direktori kerja
COPY . .
# Ekspose port yang digunakan oleh aplikasi Flask
# Ekspose port yang digunakan oleh aplikasi Flask
EXPOSE 80
# Setel command default untuk menjalankan aplikasi
CMD ["gunicorn"  , "-b", "0.0.0.0:8080", "app.py"]
