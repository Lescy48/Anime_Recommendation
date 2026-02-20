from flask import Flask, render_template, request, jsonify
import sqlite3
import requests

app = Flask(__name__)
DB_PATH = "anime.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    genres = conn.execute("SELECT DISTINCT name FROM genres ORDER BY name").fetchall()
    conn.close()
    return render_template("index.html", genres=[g["name"] for g in genres])

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    selected_genres = data.get("genres", [])
    if not selected_genres:
        return jsonify([])

    conn = get_db()
    placeholders = ",".join("?" * len(selected_genres))
    query = f"""
        SELECT a.id, a.title, a.synopsis, a.rating, a.image_url,
               (
                   SELECT GROUP_CONCAT(g2.name, ', ')
                   FROM anime_genres ag2
                   JOIN genres g2 ON ag2.genre_id = g2.id
                   WHERE ag2.anime_id = a.id
               ) as genres,
               COUNT(DISTINCT ag.genre_id) as match_count
        FROM anime a
        JOIN anime_genres ag ON a.id = ag.anime_id
        WHERE ag.genre_id IN (
            SELECT id FROM genres WHERE name IN ({placeholders})
        )
        GROUP BY a.id
        ORDER BY match_count DESC, a.rating DESC
    """
    rows = conn.execute(query, selected_genres).fetchall()
    conn.close()

    result = []
    for row in rows:
        result.append({
            "title": row["title"],
            "synopsis": row["synopsis"],
            "rating": row["rating"],
            "image_url": row["image_url"] or "",
            "genres": row["genres"],
            "match_count": row["match_count"]
        })
    return jsonify(result)

@app.route("/get-image/<path:title>")
def get_image(title):
    conn = get_db()

    row = conn.execute("SELECT image_url FROM anime WHERE title = ?", (title,)).fetchone()

    if row and row["image_url"]:
        conn.close()
        return jsonify({"image": row["image_url"]})

    try:
        res = requests.get(
            f"https://api.jikan.moe/v4/anime?q={title}&limit=1",
            timeout=5
        )
        data = res.json()
        img = data["data"][0]["images"]["jpg"]["image_url"]
        conn.execute("UPDATE anime SET image_url = ? WHERE title = ?", (img, title))
        conn.commit()
        conn.close()
        return jsonify({"image": img})
    except:
        conn.close()
        return jsonify({"image": ""})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)