from flask import Flask

app = Flask(__name__)

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

@app.route("/")
def home():
    return "Hello DevSecOps"

if __name__ == "__main__":
    app.run()