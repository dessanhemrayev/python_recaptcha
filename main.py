from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Replace with your own keys
RECAPTCHA_SITE_KEY = "your-site-key"
RECAPTCHA_SECRET_KEY = "your-secret-key"


@app.route("/")
def index():
    return render_template("index.html", site_key=RECAPTCHA_SITE_KEY)


@app.route("/submit", methods=["POST"])
def submit():
    recaptcha_response = request.form.get("g-recaptcha-response")

    # Verify the reCAPTCHA response
    payload = {"secret": RECAPTCHA_SECRET_KEY, "response": recaptcha_response}
    response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify", data=payload
    )
    result = response.json()

    if result.get("success"):
        return "Form submitted successfully!"
    else:
        return "reCAPTCHA verification failed. Please try again."


if __name__ == "__main__":
    app.run(debug=True)
