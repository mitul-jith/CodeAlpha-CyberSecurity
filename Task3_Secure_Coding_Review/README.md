# Secure Coding Review

## Overview

This project demonstrates the identification, analysis, and remediation of a SQL Injection vulnerability in a Python login application.

The project was completed as part of the CodeAlpha Cyber Security Internship.

---

## Objectives

* Identify insecure coding practices
* Demonstrate SQL Injection vulnerability
* Implement secure coding techniques
* Document findings and remediation steps

---

## Project Structure

```text
Task3_Secure_Coding_Review
│
├── vulnerable_app
├── fixed_app
├── audit_report
└── screenshots
```

---

## Vulnerability Identified

### SQL Injection

The vulnerable application directly incorporated user input into SQL queries using string interpolation.

Risk:

* Authentication bypass
* Unauthorized access
* Data disclosure

---

## Remediation

The vulnerability was fixed using parameterized SQL queries.

Example:

```python
query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))
```

---

## Evidence

The project includes:

* Vulnerable source code
* Secure source code
* Attack demonstration screenshots
* Security audit report

---

## Outcome

The secure implementation successfully prevents the demonstrated SQL Injection attack and follows secure coding best practices.
