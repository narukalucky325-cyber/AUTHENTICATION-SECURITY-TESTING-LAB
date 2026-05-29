# AUTHENTICATION-SECURITY-TESTING-LAB
A cybersecurity-focused authentication testing platform built with Flask. It simulates real-world login security mechanisms including encrypted password storage, brute-force detection, session handling, and live logging of authentication events. Designed as a penetration testing &amp; learning lab with a hacker-style UI ,security monitoring dashboard
## ⚙ Features
- 🔐 Secure Login & Registration System  
- 🔑 Password Hashing using bcrypt  
- 🧠 Session-Based Authentication  
- ⚠ Brute Force Attack Protection  
- 📊 Login Attempts Tracking  
- 📡 Live Authentication Logs  
- 🧾 Success & Failed Login Monitoring  
- 🎯 Simple Penetration Testing Simulation Lab  
- 🌌 Hacker-Style UI with Matrix Background  
<br>

## 🛠 Tech Stack

- Python (Flask)
- SQLite3 Database
- HTML5
- CSS3
- JavaScript
- bcrypt (Password Security)

<br>
## 🚀 Installation & Setup

### 1️⃣ Clone the repository
<br>
git clone https://github.com/narukalucky325-cyber/AUTHENTICATION-SECURITY-TESTING-LAB.git
<br>

## 2️⃣ Move into project folder<br>
cd AUTHENTICATION-SECURITY-TESTING-LAB
<br>
3️⃣ Install dependencies
pip install flask flask-bcrypt
<br>
4️⃣ Run the project
python app.py
<br>
5️⃣ Open in browser
http://127.0.0.1:5000
<br>
🔐 Security Features Explained
<br>

Passwords are hashed using bcrypt before storing in database
Login attempts are tracked to prevent brute-force attacks
Accounts lock after multiple failed attempts
Session-based authentication ensures secure access
Logs track all login activities in real-time

<br>
📊 Dashboard Features
<br>
Shows total successful logins
Shows failed login attempts
Displays live authentication logs
Security status monitoring (SAFE / ALERT / WARNING)
<br>
🎯 Purpose of Project
<br>

This project is designed for:

Learning web security fundamentals
Understanding authentication systems
Practicing penetration testing concepts
Building SOC-style monitoring dashboards
<br>
⚠ Disclaimer
<br>

This project is for educational purposes only.
It should not be used in production without proper security auditing and improvements.

<br>
👨‍💻 Author
<br>

Developed as a cybersecurity learning project focused on authentication security and penetration testing concepts.

<br>
⭐ If you like this project

Give it a star ⭐ on GitHub to support development!
