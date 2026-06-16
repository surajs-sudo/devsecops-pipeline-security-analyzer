# DevSecOps Pipeline Security Analyzer

## Project Overview

This project demonstrates a DevSecOps CI/CD security pipeline using GitHub Actions.

The pipeline automatically scans application code, dependencies, infrastructure configuration, and hardcoded secrets before deployment.

Integrated security tools:

* Checkov
* Trivy Vulnerability Scanner
* Trivy Secret Scanner

The goal is to implement Shift-Left Security and identify security risks early in the Software Development Life Cycle (SDLC).

---

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── security-scan.yml
│
├── sample-app/
│   ├── app.py
│   └── requirements.txt
│
├── terraform/
│   └── main.tf
│
├── .gitignore
└── README.md
```

---

## Security Tools Used

### 1. Checkov

Checkov is used for Infrastructure as Code (IaC) security scanning.

Scans for:

* Publicly exposed cloud resources
* Missing encryption
* Missing logging configuration
* Security misconfigurations
* Compliance violations

---

### 2. Trivy Vulnerability Scanner

Trivy scans application dependencies and packages.

Scans for:

* Known CVEs
* Outdated libraries
* Vulnerable package versions
* Dependency security risks

Detected vulnerable packages:

* Flask 1.0
* Requests 2.18.0
* Django 2.0

---

### 3. Trivy Secret Scanner

Trivy Secret Scanner detects sensitive information exposed in source code.

Scans for:

* AWS Access Keys
* AWS Secret Keys
* GitHub Personal Access Tokens
* API Keys
* Hardcoded Credentials

---

## GitHub Actions Workflow

The security pipeline automatically executes the following steps:

1. Checkout Repository
2. Run Checkov Scan
3. Run Trivy Vulnerability Scan
4. Run Trivy Secret Scan
5. Generate Security Findings
6. Display Security Reports

---

## Sample Security Issues Included

### Vulnerable Dependencies

Located in:

```text
sample-app/requirements.txt
```

Example:

```text
flask==1.0
requests==2.18.0
django==2.0
```

---

### Hardcoded Secrets

Located in:

```text
sample-app/app.py
```

Examples:

* AWS Access Key
* AWS Secret Access Key
* GitHub Personal Access Token

---

### Terraform Misconfiguration

Located in:

```text
terraform/main.tf
```

Example:

* Public S3 Bucket
* Public Access Enabled
* Missing Encryption
* Missing Logging

---

## Scan Results

| Tool                        | Findings                                |
| --------------------------- | --------------------------------------- |
| Checkov                     | 11 Terraform Security Misconfigurations |
| Trivy Vulnerability Scanner | 23 Dependency Vulnerabilities           |
| Trivy Secret Scanner        | 1 Critical GitHub Personal Access Token |

---

## Example Secret Detection

```text
CRITICAL: GitHub Personal Access Token

File:
sample-app/app.py

Line:
8

Severity:
CRITICAL
```

---

## DevSecOps Benefits

* Shift Left Security
* Automated Security Testing
* Early Vulnerability Detection
* Infrastructure Security Validation
* Secret Detection Before Deployment
* Continuous Security Monitoring
* Secure CI/CD Pipeline

---

## Technologies Used

* GitHub Actions
* Python
* Terraform
* Checkov
* Trivy
* YAML

---

## Future Enhancements

* GitLeaks Integration
* Docker Image Security Scanning
* SAST Integration
* DAST Integration
* Security Dashboard Reporting
* Automated Remediation

---

## Author

**Suraj Somkuwar**

DevSecOps Pipeline Security Analyzer Project
