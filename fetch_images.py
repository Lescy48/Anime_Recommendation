import sqlite3
import requests
import time
import os

DB_PATH = "anime.db"
IMG_DIR = "static/images"

def fetch_and_download_all():
    os.makedirs(IMG_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    animes = c.execute("SELECT id, title FROM anime").fetchall()
    total = len(animes)
    print(f"Downloading gambar untuk {total} anime...\n")

    for i, (anime_id, title) in enumerate(animes, 1):
        # Nama file aman
        safe_name = "".join(c2 if c2.isalnum() or c2 in " -_" else "_" for c2 in title).strip()
        img_path = f"{IMG_DIR}/{safe_name}.jpg"
        local_url = f"/static/images/{safe_name}.jpg"

        # Skip kalau udah ada
        if os.path.exists(img_path):
            c.execute("UPDATE anime SET image_url = ? WHERE id = ?", (local_url, anime_id))
            conn.commit()
            print(f"[{i}/{total}] SKIP (sudah ada)  {title}")
            continue

        try:
            # Fetch URL gambar dari Jikan
            res = requests.get(
                f"https://api.jikan.moe/v4/anime?q={title}&limit=1",
                timeout=10
            )
            data = res.json()
            img_url = data["data"][0]["images"]["jpg"]["large_image_url"]

            # Download gambarnya
            img_res = requests.get(img_url, timeout=10)
            if img_res.status_code == 200:
                with open(img_path, "wb") as f:
                    f.write(img_res.content)
                c.execute("UPDATE anime SET image_url = ? WHERE id = ?", (local_url, anime_id))
                conn.commit()
                print(f"[{i}/{total}] OK  {title}")
            else:
                print(f"[{i}/{total}] FAIL (gambar gagal download)  {title}")

        except Exception as e:
            print(f"[{i}/{total}] FAIL  {title} -> {e}")

        time.sleep(0.4)

    conn.close()
    print(f"\nSelesai! Gambar tersimpan di folder static/images/")

if __name__ == "__main__":
    fetch_and_download_all()