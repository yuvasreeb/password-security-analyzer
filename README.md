# Password Security Analyzer

A web-based password security analyzer built using **Python Flask, HTML, CSS, JavaScript, and SQLite**.

The application evaluates password strength using multiple security rules, detects previously used passwords, and generates stronger password alternatives.

## Features

- Password strength analysis
- Security rule validation
- Strength percentage calculation
- Weak, Fair, Strong, and Very Strong classification
- Password reuse detection
- Password history tracking
- SHA-256 hashing for stored passwords
- Stronger password generation
- Copy generated password
- Responsive dark-themed interface
- Local SQLite database

## Technologies Used

- **Python**
- **Flask**
- **HTML5**
- **CSS3**
- **JavaScript**
- **SQLite**
- **SHA-256**

## How It Works

1. Enter a password.
2. The application checks multiple security rules.
3. A password strength percentage is calculated.
4. The application checks whether the password was previously used.
5. A stronger password alternative can be generated.
6. Password history is stored using SHA-256 hashes instead of plain-text passwords.

## Screenshots

### Password Analyzer

![Password Analyzer](Screenshot-1.png)

### Password Analysis

![Password Analysis](screenshot-2.png)

### Password Saved

![Password Saved](screenshot-3.png)

## Project Structure

```text
password-security-analyzer/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── saved.html
│
├── app.py
├── database.db
├── requirements.txt
└── .gitignore
