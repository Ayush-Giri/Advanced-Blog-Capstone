from flask import Flask
from flask import render_template
from flask import request
import requests
import smtplib

EMAIL = "email"
PASSWORD = "password"
app = Flask(__name__)

blog_data_endpoint = "https://api.npoint.io/73ebeb8f18f601de206f"
response = requests.get(url=blog_data_endpoint)
blog_final_data = response.json()


@app.route('/')
def home():
    return render_template("index.html", blog_data=blog_final_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="password", msg=f"Subject:Fan email\n\n{name}\n{email}\n{message}")
        connection.close()
        return "<h1>Sent your message successfully </h1>"
    elif request.method == "GET":
        return render_template("contact.html")


@app.route('/post/<int:index>')
def get_post(index):
    if index == 1:
        post_data = blog_final_data[0]
        return render_template("post.html", blog_data=post_data)
    elif index == 2:
        post_data = blog_final_data[1]
        return render_template("post.html", blog_data=post_data)
    elif index == 3:
        post_data = blog_final_data[2]
        return render_template("post.html", blog_data=post_data)
    else:
        post_data = blog_final_data[3]
        return render_template("post.html", blog_data=post_data)


if __name__ == "__main__":
    app.run(debug=True)


