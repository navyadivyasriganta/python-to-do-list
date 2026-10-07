from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path(__file__).with_name("todo.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    conn.close()
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    return render_template("index.html", tasks=tasks, total=total, completed=completed)

@app.post("/add")
def add_task():
    title = request.form.get("title", "").strip()
    if title:
        conn = get_db()
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()
        conn.close()
    return redirect(url_for("index"))

@app.post("/toggle/<int:task_id>")
def toggle_task(task_id):
    conn = get_db()
    conn.execute(
        "UPDATE tasks SET completed = CASE completed WHEN 0 THEN 1 ELSE 0 END WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.post("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.post("/clear-completed")
def clear_completed():
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE completed = 1")
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
