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

## Current Scanning Limitations

While the DevSecOps pipeline provides automated security validation, there are some limitations in the current implementation:

### Checkov Limitations

* Checkov is currently configured to scan only the `terraform/` directory.
* Terraform files placed outside the `terraform/` folder will not be analyzed.
* Non-Terraform infrastructure definitions are not scanned.

### Trivy Vulnerability Scan Limitations

* The vulnerability scan primarily analyzes dependencies defined in `requirements.txt`.
* Dependencies installed outside the managed dependency file may not be detected.
* Runtime vulnerabilities are not evaluated.

### Trivy Secret Scan Limitations

* Trivy Secret Scanner analyzes repository files but may not detect secrets embedded inside binary files.
* Files such as PDFs, images, archives, and encrypted documents may not be fully inspected for hidden credentials.
* Secrets stored outside the repository are not scanned.

### General Limitations

* The workflow is configured using `soft_fail: true`, allowing the pipeline to complete even when security findings are detected.
* Security findings are reported but do not currently block code deployment.
* The project demonstrates static security testing and does not include runtime security monitoring.
* Container image scanning and cloud-native security monitoring are not implemented in the current version.


## Author

**Suraj Somkuwar**

DevSecOps Pipeline Security Analyzer Project
