from flask import Flask

app = Flask(__name__)

AWS_SECRET_ACCESS_KEY = "my-super-secret-key"

@app.route("/")
def home():
    return "Hello DevSecOps"

if __name__ == "__main__":
    app.run()