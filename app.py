
from flask import Flask, request, render_template,session
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


@app.route("/", methods=['POST','GET'])
def index_handle():
    if request.method == "GET":
        return render_template("it_tieba.html")
    # elif request.method == "POST":





@app.route("/login", methods=['POST','GET'])
def login_handle():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        userName = request.form.get("userName")
        password = request.form.get("password")

        # print(uname, upass)

        # if not (uname and uname.strip() and upass and upass.strip()):
        #     abort(Response("登录失败！"))

        # if not re.fullmatch("[a-zA-Z0-9_]{4,20}", uname):
        #     abort(Response("用户名不合法！"))

        # # 密码长度介于6-15
        # if not (len(upass) >= 6 and len(upass) <= 15):
        #     abort(Response("密码不合法！"))


        db.session.execute("SELECT * FROM student WHERE userName=%s", (userName,))
        res =db.session.fetchone()

        if res:
            # 登录成功就跳转到用户个人中心
            session["user_info"] = {
                "uid": res[0],
                "userName": res[1],
                "password": res[2],
                "email": res[3],
            }

            # return redirect(url_for("zhuye.html"))
            return render_template("/")
        else:
            # 登录失败
            return render_template("/login", login_fail=1)


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
