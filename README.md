🛡️ SentinelShield – Advanced Intrusion Detection & Web Protection System
📌 Project Overview

SentinelShield is a Python-based mini Intrusion Detection and Web Protection System that simulates the core functionality of a Web Application Firewall (WAF).
It inspects incoming HTTP requests, detects malicious patterns, monitors abusive traffic behavior, and generates security logs for analysis.

This project is designed for educational and practical learning purposes, helping students understand how real-world web security systems operate.

🎯 Objectives

Detect common web-based attacks using signature-based detection

Analyze HTTP requests for malicious content

Prevent brute-force and flooding attacks using rate limiting

Generate security logs similar to SOC environments

Understand the workflow of Detection → Decision → Logging → Analysis

🧠 Key Features

✅ SQL Injection Detection

✅ Cross-Site Scripting (XSS) Detection

✅ Command Injection Detection

✅ Directory Traversal Detection

✅ Local File Inclusion (LFI) Detection

✅ IP-based Rate Limiting

✅ Automatic Security Logging

🛠️ Technologies Used

Python 3

Flask (Web framework)

Regular Expressions (Regex) for attack signatures

File-based Logging

📁 Project Structure
SentinelShield/
│
├── sentinelsheild.py     # Main Python application
├── security.log          # Generated security logs
├── SentinelShield_Project.pptx   # Project presentation
└── README.md             # Project documentation

▶️ How to Run the Project
1️⃣ Install Required Library
pip install flask

2️⃣ Run the Application
python sentinelsheild.py

3️⃣ Access the Application

Open your browser and visit:

http://127.0.0.1:5000

🧪 Testing the System
✅ Normal Request
http://127.0.0.1:5000/?name=swapnil


✔ Request Allowed

❌ SQL Injection Test
http://127.0.0.1:5000/?id=1 OR 1=1


🚨 Blocked – SQL Injection detected

❌ XSS Test
http://127.0.0.1:5000/?q=<script>alert(1)</script>


🚨 Blocked – XSS detected

❌ Rate Limiting Test

Refresh the page more than 5 times within 10 seconds

🚨 Blocked – Rate limit exceeded

📄 Security Logs

All events are stored in security.log with the following format:

YYYY-MM-DD HH:MM:SS | IP:<address> | Attack:<type> | Status:<Allowed/Blocked>

Example:
2026-01-27 10:16:05 | IP:127.0.0.1 | Attack:SQL Injection | Status:Blocked

📊 Output & Observations

Allowed vs Blocked requests

Detected attack categories

Repeated IP activity

Rate-limited abusive behavior

These outputs help simulate real-world SOC analysis.

🧾 Academic Use

This project is suitable for:

Cybersecurity practicals

Mini projects

IDS / WAF demonstrations

Viva and internal evaluations

🚀 Future Enhancements

Web-based dashboard

Database-based logging

IP blacklisting

Machine learning–based detection

Authentication & access control

👨‍💻 Author

Swapnil Govind Pathak
Cybersecurity Student

📜 Disclaimer

This project is intended only for educational purposes.
Do not deploy in production environments without proper security review
