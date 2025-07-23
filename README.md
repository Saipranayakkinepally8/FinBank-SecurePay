# FinBank Secure Pay 💸🔐

A simulated secure payment API system for financial applications — built with security-first DevSecOps practices. This project is designed to demonstrate real-world CI/CD pipelines, security integrations, and modern DevOps tools using **100% free tools**.

---

## 🚀 Tech Stack

- **FastAPI** – Lightweight Python API framework
- **Docker** – Containerized deployment
- **Trivy** – Vulnerability scanning for images and dependencies
- **Snyk CLI** – Python dependency scanning (optional)
- **GitHub Actions** – CI/CD automation
- **Dependabot** – Automated dependency updates
- **Terraform (upcoming)** – Infra-as-code for AWS deployment

---

## 📁 Folder Structure

FinBank-securePay/
│
├── app/
│ └── main.py # FastAPI app code
│
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image setup
├── .github/
│ └── workflows/
│ └── ci.yml # GitHub Actions pipeline
│
├── snyk_report.json # (optional) Snyk scan results
├── trivy_report.json # Trivy scan results
└── README.md # You’re reading it!

yaml
Copy
Edit

---

## ⚙️ How It Works

1. **FastAPI** serves a mock payment endpoint.
2. **Docker** builds the image and runs the app locally at `http://localhost:8000`.
3. **Trivy** scans for vulnerabilities in Docker image and Python dependencies.
4. **GitHub Actions** automates CI pipeline:
   - Build & test
   - Run Trivy scans
   - Report vulnerability status in PRs
5. **Dependabot** automatically checks for dependency updates.

---

## 🔐 Security Notes

This project uses `python:3.11-slim` as base image. Some low-level system packages like `zlib1g` may have known vulnerabilities (e.g., `CVE-2023-45853`) which currently **have no upstream fixes**. This project is strictly for **demo and learning purposes**, not production use.

---

## 🛠️ Setup Instructions

**To Run Locally:**

```bash
git clone https://github.com/<your-username>/FinBank-securePay.git
cd FinBank-securePay
docker build -t fin-bank-api .
docker run -p 8000:8000 fin-bank-api
App runs at: http://localhost:8000

🔄 CI/CD Pipeline
Whenever you push code:

Docker image is built

Trivy scan is triggered

(Optional) Snyk scan is run

Results are logged in GitHub Actions tab

🎯 Goal of the Project
To showcase DevSecOps understanding and practical application using real-world tools. This is Project #2 in a personal DevOps roadmap focused on security, automation, and cloud-native thinking.

📌 Next Plans
Deploy to AWS using Terraform

Add OpenAPI documentation

Implement JWT-based auth

Enable log monitoring

📣 Contact
Made with 💻 by Sai Pranay Akkinepally

yaml
Copy
Edit
