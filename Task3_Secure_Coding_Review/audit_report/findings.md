# Security Audit Report

## Project Overview

A security review was conducted on a Python-based login application to identify common coding vulnerabilities and recommend secure coding practices.

---

# Finding 1: SQL Injection Vulnerability

## Severity

High

## Description

The application constructed SQL queries using direct user input through string interpolation.

### Vulnerable Code

```python
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```

## Risk

An attacker could manipulate SQL queries by injecting malicious SQL statements through application input fields.

## Impact

* Authentication bypass
* Unauthorized access
* Data disclosure
* Database manipulation

## Evidence

* vulnerable_code.png
* sql_injection_demo.png

## Recommendation

Use parameterized queries to separate user input from SQL commands.

---

# Remediation

## Secure Code

```python
query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))
```

## Security Improvement

Parameterized queries ensure that user input is treated as data rather than executable SQL code.

## Verification

Testing confirmed:

1. Valid credentials successfully authenticate.
2. SQL Injection attempts are rejected.

## Evidence

* fixed_code.png
* fixed_security_verification.png

---

# Conclusion

The identified SQL Injection vulnerability was successfully remediated through the implementation of parameterized SQL queries.

The updated application follows secure coding practices and is resistant to the demonstrated SQL Injection attack.
