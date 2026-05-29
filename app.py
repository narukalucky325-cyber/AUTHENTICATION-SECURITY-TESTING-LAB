from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super-secret-key"
bcrypt = Bcrypt(app)

# ---------------- DB ----------------
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        attempts INTEGER DEFAULT 0
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        action TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- LOG FUNCTION ----------------
def add_log(user, action):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs (username, action, time) VALUES (?,?,?)",
              (user, action, str(datetime.now())[:19]))
    conn.commit()
    conn.close()

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        hashed = bcrypt.generate_password_hash(p).decode("utf-8")

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        try:
            c.execute("INSERT INTO users (username, password) VALUES (?,?)", (u, hashed))
            conn.commit()
        except:
            return "User already exists"

        conn.close()

        add_log(u, "REGISTER")
        return redirect("/login")

    return render_template("register.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        c.execute("SELECT password, attempts FROM users WHERE username=?", (u,))
        user = c.fetchone()

        if not user:
            return "User not found"

        password, attempts = user

        if attempts >= 5:
            return "Account Locked"

        if bcrypt.check_password_hash(password, p):
            c.execute("UPDATE users SET attempts=0 WHERE username=?", (u,))
            conn.commit()

            session["user"] = u
            add_log(u, "LOGIN SUCCESS")

            return redirect("/dashboard")

        else:
            c.execute("UPDATE users SET attempts = attempts + 1 WHERE username=?", (u,))
            conn.commit()

            add_log(u, "LOGIN FAILED")
            return "Login Failed"

    return render_template("login.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT username, action, time FROM logs ORDER BY id DESC LIMIT 20")
    logs = c.fetchall()

    c.execute("SELECT SUM(attempts) FROM users")
    attempts = c.fetchone()[0] or 0

    c.execute("SELECT COUNT(*) FROM logs WHERE action='LOGIN SUCCESS'")
    success = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM logs WHERE action='LOGIN FAILED'")
    failed = c.fetchone()[0]

    return render_template("dashboard.html",
                           user=session["user"],
                           logs=logs,
                           attempts=attempts,
                           success=success,
                           failed=failed)

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
    