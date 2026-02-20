# Anime Recommendation

Aplikasi web rekomendasi anime berbasis Flask dengan database SQLite.

## Requirements

- Python 3.14+
- Flask
- Requests

Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup

1. Clone repo
2. Inisialisasi database:
```bash
python database.py
```
3. Download gambar:
```bash
python fetch_images.py
```
4. Jalankan aplikasi:
```bash
python app.py
```
5. Buka browser: `http://localhost:5000`

## Fitur

- Daftar 156 anime lengkap dengan synopsis dan rating
- Filter berdasarkan genre
- Gambar cover