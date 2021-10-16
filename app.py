from flask import Flask, flash, render_template, url_for, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "b8947dde6d9375914e8e81dfd2781a5b"

posts = [
    {
        "author": "John Rock",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "11/09/2021",
    },
    {
        "author": "Matty Hyde",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "09/11/2021",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
