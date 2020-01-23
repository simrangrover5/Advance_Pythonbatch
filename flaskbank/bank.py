from flask import Flask,render_template,request
#from flask import session
#from datetime import timedelta
import sqlite3
bank = Flask(__name__)
#bank.secret_key = "#oihriefjipejfie09802832hefhijfijjouhoi"
"""@bank.before_request
def before_request():
    session.permanent = True
    bank.permanent_session_lifetime=timedelta(minutes=1)"""
'''db = sqlite3.connect('bank.db')
c = db.cursor()
c.execute('create table user(name varchar(150), email varchar(150) not null primary key, password varchar(150), cpassword varchar(150))')
c.execute('create table contact(name varchar(150), email varchar(150) not null primary key, msg varchar(150))')
c.execute('create table account(id integer primary key autoincrement, name varchar(150), dob date, adhar varchar(15), phone varchar(150), uname varchar(150), password varchar(150), amount double)')
db.commit() '''  
@bank.route('/')
def index():
    return render_template('home.html')
@bank.route('/login1/')
def login():
    return render_template('login1.html')
@bank.route('/form/')
def signin():
    return render_template('form.html')
@bank.route('/afterbanking/', methods=['GET','POST'])
def afterbanking():
    if request.method=='POST':
        email=request.form.get('email')
        pswd=request.form.get('pswd')
       

        try:
            db = sqlite3.connect('bank.db')
        except Exception as e:
            return f'{e}'
        else:
            c = db.cursor()
            c.execute('select * from user where email="{}"'.format(email))
            data = c.fetchone()
            if data:
                if pswd==data[2]:
                    #session['email']=email
                    msg = email
                    return render_template('banking.html',error=msg)
                else:
                    msg='Password is wrong'
                    return render_template('login1.html',error=msg)
            else:
                msg = 'Email does not exsist'
                return render_template('login1.html',error=msg)
@bank.route('/contact/')
def contact():
    return render_template('contact.html')
@bank.route('/withdrawl/')
def withdrawl():
    return render_template('withdrawl.html')
@bank.route('/deposit/')
def deposit():
    return render_template('deposit.html')
@bank.route('/enquiry/')
def enquiry():
    return render_template('enquiry.html')
@bank.route('/account/')
def account():
    return render_template('account.html')
@bank.route('/detail/')
def detail():
    return render_template('detail.html')
@bank.route('/aftersign/',methods=['GET','POST'])
def aftersign():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        pswd=request.form.get('pswd')
        cpswd=request.form.get('cpswd')
        #return ' {} {} {} {}'.format(name,email,pswd,cpswd)
        try:
           db = sqlite3.connect('bank.db')
        except Exception as e:
           return f'{e}'
        else:
            c=db.cursor()
            c.execute('select email from user where email="{}"'.format(email))
            data=c.fetchone()
            if data:
                msg = 'This email is already exist'
                return render_template('form.html',error=msg)
            else:
                if pswd==cpswd:
                    cmd="insert into user values('{}','{}','{}','{}')".format(name,email,pswd,cpswd)
                    c.execute(cmd)
                    db.commit()
                    msg='you can login'
                    return render_template('login1.html',error=msg)
                else:
                    msg = 'Please confirm your password'
                    return render_template('form.html',error=msg)
    else:
        msg = 'Invalid method'
        return render_template('form.html',error=msg)
@bank.route('/aftercontact/',methods=['GET','POST'])
def aftercontact():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        msg=request.form.get('msg')
        
        try:
            db = sqlite3.connect('bank.db')
        except Exception as e:
            return f'{e}'
        else:
            c=db.cursor()
            c.execute('insert into contact values("{}","{}","{}")'.format(name,email,msg))
            db.commit()
            msg = 'Your message has been sent'
            #session['name'] = name
            return render_template('see.html',error=msg,errors=name)
@bank.route('/contact/')
def hey():
    return render_template('contact.html')

@bank.route('/afteropen/',methods=['GET','POST'])
def afteropen():
    if request.method=='POST':
        name=request.form.get('name')
        dob=request.form.get('dob')
        adhar=request.form.get('adhar')
        phone=request.form.get('phone')
        uname=request.form.get('uname')
        password=request.form.get('password')
        #return ' {} {} {} {} {} {}'.format(name,dob,adhar,phone,uname,password)
        try:
            db = sqlite3.connect('bank.db')
        except Exception as e:
            return f'{e}'
        else:
            c = db.cursor()
            c.execute('insert into account(name,dob,adhar,phone,uname,password) values("{}","{}","{}","{}","{}","{}")'.format(name,dob,adhar,phone,uname,password))
            db.commit()
            msg = 'done'
            return render_template('account.html',error=msg)
            
    else:
        msg = 'Invalid method'
        return render_template('account.html',error=msg)
@bank.route('/afterdeposit/',methods=['GET','POST'])
def afterdeposit():
    if request.method=='POST':
        acnumber = request.form.get('acnumber')
        uname = request.form.get('uname')
        amount=request.form.get('amount')
        try:
            db = sqlite3.connect('bank.db')
        except Exception as e:
            return f'{e}'
        else:
            c=db.cursor()
            c.execute('select * from account where uname="{}"'.format(uname))
            data = c.fetchone()
            if data:
                c.execute('update account set amount="{}" where id="{}"'.format(amount,acnumber))
                db.commit()
                return 'done'
            else:
                return "data not found"
    else:
        msg='Invalid method'
        return render_template('deposit.html',error=msg)
@bank.route('/afterenquiry/',methods=['GET','POST'])
def afterenquiry():
    if request.method=='POST':
        uname=request.form.get('uname')
        pswd=request.form.get('pswd')
        try:
            db = sqlite3.connect('bank.db')
        except Exception as e:
            return f'{e}'
        else:
            c=db.cursor()
            c.execute('select * from account where uname="{}"'.format(uname))
            data = c.fetchone()
            return render_template('page.html',error=data)
    else:
        msg='Invalid method'
        return render_template('enquiry.html',error=msg)
@bank.route('/afterdetail/',methods=['GET','POST'])
def afterdetail():
    if request.method=='POST':
        uname = request.form.get('uname')
        pswd = request.form.get('pswd')
        newadhar=request.form.get('newadhar')
        newphone=request.form.get('newphone')
        newuname=request.form.get('newuname')
        newpswd=request.form.get('newpswd')
        try:
            db = sqlite3.connect('bank.db')
        except Exception as e:
            return f'{e}'
        else:
            c=db.cursor()
            c.execute('select * from account where uname="{}"'.format(uname))
            data = c.fetchone()
            if data:
                c.execute('update account set uname="{}",phone="{}",adhar="{}",password="{}" where uname="{}"'.format(newuname,newphone,newadhar,newpswd,uname))
                db.commit()
                return 'done'
            else:
                return "data not found"
    else:
        msg='Invalid method'
        return render_template('detail.html',error=msg)
@bank.route('/afterwithdraw/',methods=['GET','POST'])
def afterwithdraw():
    if request.method=='POST':
        username=request.form.get('username')
        pswd = request.form.get('pswd')
        amount = request.form.get('amount')
        try:
            db = sqlite3.connect('bank.db')
        except Exception as e:
            return f'{e}'
        else:
            c=db.cursor()
            c.execute('select * from account where uname = "{}"'.format(username))
            data = c.fetchone()
            if data:
                balance = data[7]
                balance = balance-float(amount)
                #return f'{balance}'
                c.execute('update account set amount = "{}" where uname="{}"'.format(balance,username))
                db.commit()
                msg = 'done'
                return msg
            else:
                return f'data not found'
    else:
        msg = 'Invalid method'
        return render_template('withdrawl.html',error=msg)
bank.run(host='localhost',port=80,debug=True)