# Regenerating the full Flask app with corrected Strategy pattern implementation

omdb_api_key = "f2cda4cbefab22bb2367fabd8e5dd3b8"  # You should replace this with your actual OMDb API key

# Final upgraded code with corrected formatting
updated_code = f"""
from flask import Flask, request, jsonify
import requests
import sqlite3
from functools import wraps

app = Flask(__name__)

# === DESIGN PATTERN: Decorator ===
def log_route(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(f"[LOG] Accessed route: {{f.__name__}}")
        return f(*args, **kwargs)
    return decorated_function

# === DESIGN PATTERN: Factory ===
class Movie:
    def __init__(self, title, year, genre, director):
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director

    def to_dict(self):
        return {{
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "director": self.director
        }}

class MovieFactory:
    @staticmethod
    def create_movie(data):
        return Movie(
            title=data.get("Title"),
            year=data.get("Year"),
            genre=data.get("Genre"),
            director=data.get("Director")
        )

# === DESIGN PATTERN: Strategy ===
class ReportStrategy:
    def generate(self, user_movies):
        raise NotImplementedError

class JSONReport(ReportStrategy):
    def generate(self, user_movies):
        return {{
            "total_movies": len(user_movies),
            "movies": user_movies
        }}

class PlainTextReport(ReportStrategy):
    def generate(self, user_movies):
        lines = [f"- {{movie}}" for movie in user_movies]
        return "\\n".join(lines)

# === Database Initialization ===
def init_db():
    conn = sqlite3.connect("moviemate.db")
    cursor = conn.cursor()
    cursor.execute(\"""
        CREATE TABLE IF NOT EXISTS watchlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            movie_title TEXT
        )
    \""")
    cursor.execute(\"""
        CREATE TABLE IF NOT EXISTS preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            genre TEXT,
            actor TEXT
        )
    \""")
    conn.commit()
    conn.close()

# === ROUTES ===

@app.route("/")
@log_route
def home():
    return jsonify({{
        "message": "Welcome to MovieMate API!",
        "endpoints": ["/preferences", "/watchlist", "/recommendations", "/omdb", "/report"]
    }})

@app.route("/preferences", methods=["POST"])
@log_route
def save_preferences():
    data = request.json
    user = data.get("user")
    genre = data.get("genre")
    actor = data.get("actor")

    conn = sqlite3.connect("moviemate.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO preferences (user, genre, actor) VALUES (?, ?, ?)", (user, genre, actor))
    conn.commit()
    conn.close()

    return jsonify({{"message": "Preferences saved successfully"}})

@app.route("/preferences", methods=["GET"])
@log_route
def get_preferences():
    user = request.args.get("user")
    conn = sqlite3.connect("moviemate.db")
    cursor = conn.cursor()
    cursor.execute("SELECT genre, actor FROM preferences WHERE user = ? ORDER BY id DESC LIMIT 1", (user,))
    row = cursor.fetchone()
    conn.close()
    return jsonify({{"preferences": row if row else "Not found"}})

@app.route("/watchlist", methods=["POST"])
@log_route
def add_to_watchlist():
    data = request.json
    user = data.get("user")
    movie_title = data.get("movie_title")

    conn = sqlite3.connect("moviemate.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO watchlist (user, movie_title) VALUES (?, ?)", (user, movie_title))
    conn.commit()
    conn.close()
    return jsonify({{"message": "Movie added to watchlist"}})

@app.route("/watchlist", methods=["GET"])
@log_route
def get_watchlist():
    user = request.args.get("user")
    conn = sqlite3.connect("moviemate.db")
    cursor = conn.cursor()
    cursor.execute("SELECT movie_title FROM watchlist WHERE user = ?", (user,))
    rows = cursor.fetchall()
    conn.close()
    return jsonify({{"watchlist": [row[0] for row in rows]}})

@app.route("/omdb", methods=["GET"])
@log_route
def get_movie_from_omdb():
    title = request.args.get("title")
    url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={{title}}"
    response = requests.get(url)
    data = response.json()
    if data.get("Response") == "True":
        movie = MovieFactory.create_movie(data)
        return jsonify(movie.to_dict())
    else:
        return jsonify({{"error": "Movie not found"}}), 404

@app.route("/report", methods=["GET"])
@log_route
def report():
    user = request.args.get("user")
    fmt = request.args.get("format", "json")

    conn = sqlite3.connect("moviemate.db")
    cursor = conn.cursor()
    cursor.execute("SELECT movie_title FROM watchlist WHERE user = ?", (user,))
    movies = [row[0] for row in cursor.fetchall()]
    conn.close()

    strategy = JSONReport() if fmt == "json" else PlainTextReport()
    report_result = strategy.generate(movies)
    return jsonify(report_result) if fmt == "json" else report_result

# === MAIN ===
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5001)
"""

# Save final updated file
output_path = "/mnt/data/moviemate_flask_api_m4.py"
with open(output_path, "w") as f:
    f.write(updated_code)

output_path