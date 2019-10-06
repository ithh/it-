
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/mydb?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "student"
    sno = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, sname, email):
        self.sname = sname
        self.email = email

    def __repr__(self):
        return '<Student %r>' % self.sname

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
    elif request.method == "POST":
        sname = request.form.get("sname")
        email = request.form.get("email")
        print(sname, email)
        stu = Student(sname, email)
        db.session.add(stu)
        db.session.commit()

        return "注册成功"


if __name__ == '__main__':
    app.run(debug=True)
