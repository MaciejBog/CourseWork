from flask import Flask, render_template, url_for, request
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

API_ENDPOINT = os.getenv("API_ENDPOINT")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP = os.getenv("SMTP")

app = Flask(__name__)

blog_request = requests.get(API_ENDPOINT)
print(blog_request.status_code)
blog_data = blog_request.json()

@app.route("/")
def home():
    return render_template("index.html", data=blog_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", msg_sent=False)
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="",
                                msg=f"Subject:New Form Submission\n\nA new form submission came through!\n"
                                    f"Name: {name}\n"
                                    f"Email: {email}\n"
                                    f"Phone: {phone}\n"
                                    f"Message: {message}"
                                )
        return render_template("contact.html", msg_sent=True)

@app.route("/post/<id>")
def post(id):
    post_data = blog_data[int(id) - 1]
    title = post_data["title"]
    subtitle = post_data["subtitle"]
    post = post_data["body"]
    return render_template("post.html", title=title,subtitle=subtitle,post=post)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
