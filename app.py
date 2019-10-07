
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/mydb?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "student"
    # sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(80), primary_key=True, unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, userName, password, email):
        self.userName = userName
        self.password = password
        self.email = email

    # def __repr__(self):
    #     return '<Student %r>' % self.userName
    # def __iter__(self):
    #     return '<Student %r>' % self.userName
# db.create_all()


@app.route("/")
def index_handle():
    if request.method == "GET":
        return render_template("it_tieba.html")

@app.route("/login", methods=['POST','GET'])
def login_handle():
    if request.method == "GET":
        return render_template("login.html")
    # elif request.method == "POST":
    #     userName = request.form.get("userName")
    #     password = request.form.get("password")


@app.route("/register", methods=['POST','GET'])
def reg_handle():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        userName = request.form.get("userName")
        # result = Student.query.filter(Student.userName == "%s" , (userName,)).first()
        # if result == 0:
        #     return "用户名已注册"
        password = request.form.get("password")
        email = request.form.get("email")
        # print(userName,password, email)
        stu = Student(userName, password, email)
        db.session.add(stu)
        db.session.commit()

        return "注册成功"


if __name__ == '__main__':
    app.run(debug=True)
