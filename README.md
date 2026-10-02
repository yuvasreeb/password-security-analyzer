# Password Security Analyzer

A simple web-based tool that evaluates password strength and checks password reuse.

## 🚀 Live Demo

https://password-security-analyzer-cysz.onrender.com

## ✨ Features

- Password strength analysis
- Security rule checking
- Strength percentage
- Password reuse detection
- SHA-256 password hashing
- Password history using SQLite
- Stronger password generator
- Copy generated password

## 🛠️ Technologies

- HTML
- CSS
- Python
- Flask
- SQLite

 📁 Project Structure

password-security-analyzer/
├── app.py
├── database.db
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── result.html
    └── saved.html

## Security Note

The application uses SHA-256 hashing for passwords stored in the password history database. Plain-text passwords are not stored.

## Project Purpose

This project was developed as an internship project to demonstrate practical implementation of:

- Python Flask web development
- Frontend and backend integration
- Password security concepts
- SQLite database integration
- Password strength evaluation
- Secure password history handling
- JavaScript-based password generation

The application checks whether a password was previously used without storing the original password.

