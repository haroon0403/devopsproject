from flask import Flask
import psycopg2
from datetime import datetime
import os

app = Flask(__name__)

DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "appdb")
DB_USER = os.getenv("POSTGRES_USER", "appuser")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "apppass")
LOG_FILE = "/shared/log.txt"

def log_to_db(message):
    conn = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS messages (id SERIAL PRIMARY KEY, message TEXT);")
    cur.execute("INSERT INTO messages (message) VALUES (%s);", (message,))
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def home():
    msg = f"Accessed backend at {datetime.now()}"
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")
    log_to_db(msg)
    return "Hello from Flask Backend with PostgreSQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

