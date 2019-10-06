from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_handle():
    if request.method == "GET":
        return render_template("it_tieba.html")

@app.route("/login")
def login_handle():
    if request.method == "GET":
        return render_template("login.html")

@app.route("/register")
def reg_handle():
    if request.method == "GET":
        return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
