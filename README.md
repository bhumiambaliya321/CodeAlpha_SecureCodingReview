# 🔐 Secure Coding Review

> **CodeAlpha Cyber Security Internship - Task 3**

## 📖 Project Overview

This project was completed as part of the **CodeAlpha Cyber Security Internship**.

The objective of this project is to identify common security vulnerabilities in source code, understand their impact, and implement secure coding practices to protect applications from cyber attacks.

The project demonstrates how an insecure SQL query can lead to **SQL Injection** and how **Parameterized Queries** can prevent this vulnerability.

---

## 🎯 Objectives

* Review vulnerable source code
* Identify security issues
* Understand SQL Injection attacks
* Implement secure coding techniques
* Improve application security using best practices

---

## 🛠 Technologies Used

* Python 3
* SQLite3
* Visual Studio Code
* Git
* GitHub
* Bandit (Static Code Analysis)

---

## 📂 Project Structure

```text
CodeAlpha_SecureCodingReview/

├── vulnerable_code.py
├── secure_code.py
├── create_database.py
├── users.db
├── Secure_Coding_Review_Report.pdf
├── screenshots/
└── README.md
```

---

## ⚠ Vulnerability Demonstrated

### SQL Injection

The vulnerable application directly concatenates user input into an SQL query.

Example:

```python
query = "SELECT * FROM users WHERE username='" + username + "'"
```

Example malicious input:

```text
' OR '1'='1
```

This may allow attackers to manipulate SQL queries and bypass authentication.

---

## ✅ Secure Implementation

The secure version uses **Parameterized Queries**.

Example:

```python
query = "SELECT * FROM users WHERE username=?"

cursor.execute(query, (username,))
```

This separates user input from the SQL statement and prevents SQL Injection attacks.

---

## 📊 Security Findings

| Vulnerability               | Risk Level | Solution              |
| --------------------------- | ---------- | --------------------- |
| SQL Injection               | High       | Parameterized Queries |
| Missing Input Validation    | Medium     | Validate User Input   |
| Insecure Query Construction | High       | Prepared Statements   |

---

## 🔒 Secure Coding Best Practices

* Validate all user input.
* Use parameterized SQL queries.
* Never trust user input.
* Avoid hardcoded credentials.
* Handle exceptions properly.
* Keep software updated.
* Perform regular code reviews.
* Use static analysis tools.
* Follow OWASP Secure Coding Guidelines.

---

## 📚 Learning Outcomes

Through this project, I learned:

* Secure coding principles
* SQL Injection prevention
* Database security basics
* Static code analysis
* Cybersecurity best practices

---

## 📸 Project Output

✔ Vulnerable Python Code

✔ Secure Python Code

✔ SQLite Database

✔ Security Review Report

✔ SQL Injection Demonstration

✔ GitHub Repository

---

## 👨‍💻 Internship Details

**Organization:** CodeAlpha

**Domain:** Cyber Security

**Task:** Secure Coding Review

---

## 📌 Conclusion

Secure coding is one of the most effective ways to protect applications from cyber threats. By using parameterized queries and following secure coding standards, developers can significantly reduce the risk of SQL Injection and other common vulnerabilities.

This project enhanced my practical understanding of application security and secure software development.

---

## ⭐ Acknowledgement

This project was completed as part of the **CodeAlpha Cyber Security Internship** to improve practical knowledge of secure software development and cybersecurity best practices.

---

### 👨‍💻 Developed By

**Bhumi Ambaliya**

Cyber Security Intern

CodeAlpha
