from flask import Flask, render_template, session, redirect, request, flash
from datetime import timedelta
import hashlib
import re
from models import dbConnect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
    'index.html'
    )




# ログインページの表示
app.route('/login')
def login():
    return render_template('registration/login.html')



# ログイン処理
@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == '' or password == '':
        flash('入力されていません')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashpassword = hashlib.she256(password.encode('utf-8')).hexdigest()
            if hashpassword != user["password"]:
                flash('パスワードが間違っています!')
            else:
                session['uid'] = user["uid"]
                return redirect('/')
    return redirect('/login')



# ログアウト処理
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')



# サインアップページの表示
@app.route('/signup')
def signup():
    return render_template('registration.html')



# サインアップの処理
@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    child_name = request.form.get('child_name')
    child_sex = request.form.get('sex')
    child_birthday = request.form.get('birthday')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if name == '' or phone_number == '' or email == '' or password1 == '' or password2 == '' or child_name == '' or child_sex == '' or child_birthday == '':
        flash('入力してください')
    elif password1 != password2:
        flash('パスワードが間違っています')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスではありません')
    else:
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        DBuser = dbConnect.getUser(email)

        if DBuser != None:
            flash('既に登録されています')
        else:
            dbConnect.createUser(uid, name, phone_number, email, password, child_name, child_sex, child_birthday)
            UserId = str(uid)
            session['uid'] = UserId
            return redirect('/')
    return redirect('/signup')



# チャンネル一覧ページの表示





if __name__ == '__main__':
    app.run (host= "0.0.0.0", debug = True)
