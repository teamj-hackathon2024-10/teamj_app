from flask import Flask, render_template, session, redirect, request, flash
from datetime import timedelta
import hashlib
import re
from models import dbConnect
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)

@app.route('/')
def userhome():
    return render_template(
    'user/userhome.html'
    )



# ログインページの表示
@app.route('/login')
def login():
    return render_template('registration/login.html')



# ログイン処理
@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')  # emailとpasswordでログインする
    password = request.form.get('password')

    if email == '' or password == '':  # emailかpasswordが空の場合表示
        flash('入力されていません')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashpassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashpassword != user["password"]:
                flash('パスワードが間違っています!')
            else:
                session['id'] = user["id"]
                if user["admin"] == 0:
                    return redirect('/')
                else:
                    return redirect('management-home')#後で@app.routeで書く
    return redirect('/login')



# ログアウト処理
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')



# サインアップページの表示
@app.route('/signup')
def signup():
    return render_template('registration/signup.html')



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
    allergies = 1

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
            print( name, email, password, phone_number, child_name, child_sex, allergies ,child_birthday)
            dbConnect.createUser( name, email, password, phone_number, child_name, child_sex, allergies ,child_birthday)
            DBuser = dbConnect.getUser(email)
            print(DBuser)
            UserId = str(DBuser['id'])
            session['id'] = UserId
            return redirect('/')
    return redirect('/signup')

@app.route('/management-home')
def managementHome():
    return render_template('management/home.html')

@app.route('/management-channels')
def managementChannels():
    return render_template('management/channels.html')


# チャンネル一覧ページの表示
@app.route('/')
def index():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    else:
        channels = dbConnect.getChannelAll()
        channels.reverse()
    return render_template('user/index.html', channels=channels, user_id=user_id, meals_id=meals_id, allergens_id=allergens_id )





# チャンネルの追加
@app.route('/', methods=['POST'])
def add_channel():
   admin = session.get('admin')
   if admin is None:
       return redirect('/login')
   channel_name = request.form.get('channelTitle')
   channel = dbConnect.getChannelByName(channel_name)
   if channel == None:
       channel_description = request.form.get('channelDescription')
       dbConnect.addChannel(admin, channel_name, channel_description)
       return redirect('/')
   else:
       error = '既に同じ名前のチャンネルがあります'
       return render_template('error/error.html', error_message=error)



# # チャンネルの更新
# @app.route('/update_channel', methods=['POST'])
# def update_channel():
#     user_id = session.get("user_id")
#     if user_id is None:
#         return redirect('/login')

#     channel_id = request.form.get('channel_id')
#     channel_name = request.form.get('channelTittle')
#     channel_description = request.form.get('channelDescription')

#     dbConnect.updateChannel('user_id, channel_name, channel_description, channel_id')
#     return redirect('/detail/{channel_id}'.format(channel_id = channel_id))



# チャンネルの削除機能
@app.route('/delete/<channels_id>')
def delete_channel(channels_id):
    admin = session.get('admin')
    if admin is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelAll(channels_id)
        if channel['admin'] != ["admin"]:
            flash('チャンネルは管理者のみ削除可能です')
            return redirect('/')
        else:
            dbConnect.getChannelAll(channels_id)
            return redirect('/')







# # メッセージの投稿!
# @app.route('/message', methods=['POST'])
# def add_message():
#     user_id = session.get('user_id')
#     if user_id is None:
#         return redirect('/login')

#     message = request.form.get('message')
#     channels_id = request.form.get('channels_id')

#     if message:
#         dbConnect.createMessage(user_id, channels_id, message)

#     return redirect('/detail/'{channels_id}.format(channels_id = channels_id))




if __name__ == '__main__':
    app.run (host= "0.0.0.0", debug = True)
