# 🎬 MovieMate

A lightweight Flask-based movie tracker app that lets users search, save, and analyze movies using the OMDb API and a local SQLite database.

---

## 📌 Overview

**MovieMate** was developed for the SFWRTECH 4SA3 Software Architecture course as a way to explore clean architecture, API integration, and design pattern usage.

- 🔍 Search for any movie using the [OMDb API](https://www.omdbapi.com/)
- 🎞️ Save favorite titles to your personal watchlist
- 📊 Generate a report of your saved movies in JSON or plain text
- 🧠 Implements 3 software design patterns:
  - Factory (Creational)
  - Decorator (Structural)
  - Strategy (Behavioral)

---

## 🛠️ Technologies Used

| Tech         | Purpose                                 |
|--------------|------------------------------------------|
| Python       | Core language                            |
| Flask        | Web API framework                        |
| SQLite       | Lightweight cloud-compatible database    |
| OMDb API     | Third-party movie data source            |
| Git          | Version control + reflection tracking    |

---

## 🚀 How to Run the App

1. Clone or unzip the project:
   ```bash
   git clone https://github.com/yourusername/moviemate.git
   cd moviemate

2. Install dependencies:

pip install flask requests

3. Run the app:

python3 moviemate_flask_api_m4.py

Access it via browser or Postman:

http://localhost:5001/

📡 API Endpoints
/omdb?title=Inception

Searches for a movie from the OMDb API.
/watchlist [POST, GET]

    POST: Add a movie to a user's watchlist

    GET: Retrieve user's saved movies

/preferences [POST, GET]

Save and retrieve user preferences (genre, actor)
/report?user=alice&format=json

Generates a watchlist report (Strategy pattern: JSON or plain text)
