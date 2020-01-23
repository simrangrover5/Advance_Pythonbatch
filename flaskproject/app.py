from flask import Flask,render_template,request,make_response
from flask import session
import pymysql as sql


app = Flask(__name__)

app.secret_key = "#oihriefjipejfie09802832hefhijfijjouhoi"

@app.route("/")
def index():
    return render_template("nav.html")
    #return "Hello world"

@app.route("/home/<var>/")
def home(var):
    return render_template("one.html",name=var)
    #return "<h1 style='color:red'>Welcome to my home {}</h1>".format(var)

@app.route("/home/<var>/<int:n1>/<int:n2>/<int:n3>")
def home1(var,n1,n2,n3):
    data = {
        'name' : var,
        'maths' : n1,
        'science' : n2,
        'english' : n3
    }
    return render_template("one.html",data=data)
    #return "Welcome to the class of flask"

@app.route("/<name>/<job>/<int:salary>/")
def match(name,job,salary):
    data = {
        'name' : name,
        'job' : job,
        'salary' : salary
    }
    return render_template("two.html",data=data,loan="yes")

@app.route("/login/")
def login():
    if request.cookies.get("email"):
        return render_template("one.html")
    else:
        return render_template("login.html")

@app.route("/afterlogin/",methods=['GET','POST'])
def afterlogin():
    email = request.form.get('email')
    password = request.form.get('pswd')
    try:
        db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch11am")
    except Exception as e:
        return f"{e}"
    else:
        c = db.cursor()
        c.execute("select * from user where email='{}'".format(email))
        data = c.fetchone()
        if password == data[2]:
            session['email'] = email
            return render_template("one.html")
            #resp = make_response(render_template("one.html"))
            #resp.set_cookie("email",email)
            #resp.set_cookie("islogin","true")
            #return resp
            #return "<h1>Email = {} and password = {}</h1>".format(email,password)
        else:
            error = "Invalid Password"
            return render_template("login.html",error=error)

@app.route("/signup/")
def signup():
    return render_template("form.html")


@app.route("/aftersign/",methods=['GET','POST'])
def aftersign():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        pswd = request.form.get("pswd")
    #return "{} {} {}".format(name,email,pswd)
        try:
            db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch11am")
        except Exception as e:
            return f"{e}"
        else:
            c = db.cursor()
            c.execute("select email from user where email='{}'".format(email))
            data = c.fetchone()
            if data:
                error = "Email already exists...."
                return render_template("form.html",error=error)
            else:
                cmd = "insert into user values('{}','{}','{}')".format(name,email,pswd)
                c.execute(cmd)
                db.commit()
                msg = "You can login now...."
                return render_template("login.html",error=msg)
    else:
        error = "Invalid method"
        return render_template("form.html",error=error)

@app.route("/logout/")
def logout():
    del session["email"]
    return render_template("login.html")
    #resp = make_response(render_template("login.html"))
    #resp.delete_cookie("email")
    #resp.delete_cookie("islogin")
    #return resp

app.run(host="localhost",port=80,debug=True)