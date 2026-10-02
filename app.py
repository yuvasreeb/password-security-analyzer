from flask import Flask, render_template, request
import hashlib
import sqlite3
import re

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_database():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS password_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password_hash TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def check_password(password):
    rules = []

    is_long = len(password) >= 12
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_number = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    common_passwords = {
        "password",
        "password123",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "admin123",
        "letmein",
        "welcome",
        "iloveyou",
        "yuva",
        "123456789"
    }

    is_not_common = password.lower() not in common_passwords

    repeated = bool(re.search(r"(.)\1\1", password))

    sequences = [
        "1234", "2345", "3456",
        "4567", "5678", "6789",
        "abcd", "bcde", "cdef",
        "defg", "qwer", "asdf"
    ]

    has_sequence = any(
        sequence in password.lower()
        for sequence in sequences
    )

    no_patterns = not repeated and not has_sequence

    # Password Rules
    rules.append({
        "text": "At least 12 characters",
        "passed": is_long
    })

    rules.append({
        "text": "Uppercase and lowercase letters",
        "passed": has_upper and has_lower
    })

    rules.append({
        "text": "Contains a number",
        "passed": has_number
    })

    rules.append({
        "text": "Contains a symbol",
        "passed": has_symbol
    })

    rules.append({
        "text": "Not a common password",
        "passed": is_not_common
    })

    rules.append({
        "text": "No repeated characters or sequences",
        "passed": no_patterns
    })

    # Password Strength Score
    strength = 0

    if is_long:
        strength += 25

    if has_upper and has_lower:
        strength += 15

    if has_number:
        strength += 15

    if has_symbol:
        strength += 15

    if is_not_common:
        strength += 15

    if no_patterns:
        strength += 15

    return rules, strength


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    password = request.form.get("password", "")

    # Hash password for history checking
    password_hash = hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()

    conn = get_db_connection()

    existing = conn.execute(
        """
        SELECT id
        FROM password_history
        WHERE password_hash = ?
        """,
        (password_hash,)
    ).fetchone()

    history = conn.execute(
        """
        SELECT id, created_at
        FROM password_history
        ORDER BY created_at DESC
        """
    ).fetchall()

    conn.close()

    already_used = existing is not None

    # Password rules
    rules,strength = check_password(password)

    # History rule
    rules.append({
        "text": "Password has not been used before",
        "passed": not already_used
    })

    
    # Strength label
    if strength < 50:
       strength_label = "Weak"
    elif strength < 70:
       strength_label = "Fair"
    elif strength < 85:
       strength_label = "Strong"
    else:
       strength_label = "Very Strong"
    return render_template(
        "result.html",
        rules=rules,
        strength=strength,
        password=password,
        strength_label=strength_label,
        already_used=already_used,
        history=history
    )
@app.route("/save-password", methods=["POST"])
def save_password():

    password = request.form.get("password", "")

    if not password:
        return "Password cannot be empty", 400

    password_hash = hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()

    conn = get_db_connection()

    try:
        conn.execute(
            """
            INSERT INTO password_history (password_hash)
            VALUES (?)
            """,
            (password_hash,)
        )

        conn.commit()

    except sqlite3.IntegrityError:
        pass

    conn.close()

    return render_template(
        "saved.html"
    )

if __name__ == "__main__":
    create_database()
    app.run(debug=True)