from flask import Flask, render_template, session, redirect, request, flash
from datetime import timedelta
import hashlib
import re
from models import dbConnect
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)


# ユーザーホーム画面の表示
@app.route('/user_home')
def userhome():
    return render_template(
    'user/userhome.html'
    )


# ログインページの表示
@app.route('/')
def login():
    return render_template('registration/login.html')



# ログイン処理
@app.route('/', methods=['POST'])
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
                if user['admin'] == 1:
                    session['admin'] = 1
                    return redirect('management-home')
                else:
                    session['admin'] = 0
                    return redirect('/user_home')
    return redirect('/')



# ログアウト処理
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



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
            dbConnect.createUser( name, email, password, phone_number, child_name, child_sex, allergies ,child_birthday)
            DBuser = dbConnect.getUser(email)
            UserId = DBuser['id']
            session['id'] = UserId
            if DBuser['admin'] == 1:
                session['admin'] = 1
                return redirect('/management-home')
            else:
                session['admin'] = 0
                return redirect('/user_home')
    return redirect('/signup')






# チャンネル一覧ページの表示
@app.route('/channels')
def index():
    user_id = session.get('id')
    admin=session.get('admin')
    if user_id is None:
        return redirect('/')
    else:
        if admin:
            channels = dbConnect.getAdminChannels()
            users = dbConnect.getAllUsers()
        else:
            channels = dbConnect.getChannels(user_id)
            users = None

        # channels.update_at()

    return render_template('common/channel.html', channels=channels, user_id=user_id,admin=admin, users=users)




# 管理者のホーム画面表示
@app.route('/management-home')
def managementHome():
    admin=session.get('admin')
    return render_template('management/home.html',admin=admin)


# # 管理者のチャンネルページの表示
# @app.route('/management-channels')
# def managementChannels():
#     user_id = session.get('id')
#     print(user_id)
#     if user_id is None:
#         return redirect('/')
#     else:
#         channels = dbConnect.getUserChannels(user_id)
#         # channels.update_at()
#     return render_template('common/channel.html', channels=channels, user_id=user_id)

# テスト処理
@app.route('/test')
def test():
    session.clear()
    return render_template('modal/update-channel-confirmation.html')


# # # 管理者チャンネル詳細ページ表示機能
# @app.route('/management-detail/<channel_id>')
# def management_detail(channel_id):
#     user_id = session.get("id")
#     if user_id is None:
#         return redirect('/')

#     cid = channel_id
#     channel = dbConnect.getChannelById(cid)
#     messages = dbConnect.getMessageAll(channel_id)

#     return render_template('common/chat.html', messages=messages, channel=channel, user_id=user_id)



# チャンネルの追加
@app.route('/management-channels', methods=['POST'])
def add_channel():
   uid = session.get('id')
   print(uid)
   if uid is None:
       return redirect('/management-home') #   管理者のホームへ移動へ変更済
   channel_name = request.form.get('channel-name')
   channel = dbConnect.getChannelByName(channel_name)
   print("check1")
   if channel == None:
       channel_id = str(uuid.uuid4())
       is_open = request.form.get('is_open', False)
       dbConnect.addChannel(channel_id, channel_name, is_open)

       target_user_id = request.form.get('target_user_id')
       if target_user_id:
           dbConnect.updateChannel(channel_id,target_user_id)
       return redirect('/channels')
   else:
       error = '既に同じ名前のチャンネルがあります'
       return render_template('error/error.html', error_message=error)


# チャンネルの削除機能
@app.route('/delete/<channel_name>')
def delete_channel(channel_name):
    admin = session.get('admin')
    if admin is None:
        return redirect('/management-home')
    else:
        channel = dbConnect.getChannelByName(channel_name)
        if channel('admin') != ("admin"):
            flash('チャンネルは管理者のみ削除可能です')
            return redirect('/channels')
        else:
            dbConnect.deleteChannel(channel_name)
            return redirect('/channels')


# # チャンネルの更新
#@app.route('/update_channel', methods=['POST'])
#def update_channel():
#     user_id = session.get("id")
#     if user_id is None:
#         return redirect('/')

#     channel_id = request.form.get('channel_id')
#     channel_name = request.form.get('channelTittle')
#     channel_description = request.form.get('channelDescription')

#     dbConnect.updateChannel('user_id, channel_name, channel_description, channel_id')
#     return redirect('/detail/{channel_id}'.format(channel_id = channel_id))



# チャンネル詳細ページ表示機能
@app.route('/detail/<channel_id>')
def detail(channel_id):
    user_id = session.get("id")
    admin=session.get('admin')
    if user_id is None:
        return redirect('/')
    cid = channel_id
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(channel_id)

    return render_template('common/chat.html', messages=messages, channel=channel, user_id=user_id,admin=admin)




#メッセージの投稿機能
@app.route('/message', methods=['POST'])
def add_message():
    user_id = session.get('id')
    if user_id is None:
        return redirect('/')

    message = request.form.get('message')
    channel_id = request.form.get('channel_id')


    if message:
        dbConnect.createMessage(user_id, channel_id, message)

    return redirect('/detail/{channel_id}'.format(channel_id = channel_id))




# ## ユーザーの基本情報編集
# #@app.route('/updateuser', methods=['POST'])
# #def update_user():
# #    user_id = session.get("user_id")
# #    if user_id is None:
# #        return redirect('/user/userhome')

# #    name = request.form.get('name')
# #    phone_number = request.form.get('phone_number')
# #    email = request.form.get('email')
# #    password = request.form.get('password')
#     child_name = request.form.get('child_name')
#     child_sex = request.form.get('sex')
#     child_birthday = request.form.get('birthday')
#     allergies = 1

#     pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

#     if name == '' or phone_number == '' or email == '' or password == '' or child_name == '' or child_sex == '' or child_birthday == '':
#         flash('入力してください')
#     elif re.match(pattern, email) is None:
#         flash('正しいメールアドレスではありません')
#     else:
#         password = hashlib.sha256(password.encode('utf-8')).hexdigest()

#         print( name, email, password, phone_number, child_name, child_sex, allergies ,child_birthday)
#         dbConnect.updateUser( name, email, password, phone_number, child_name, child_sex, allergies ,child_birthday)
#         DBuser = dbConnect.getUser(user_id)
#         session['id'] = DBuser['id']
#         return redirect('/user_home')
#     return render_template('/user/user_information.html', user_id = user_id)






## 子供のアレルギー原因食品
#@app.route('/allergens/<allergen_id>')
#def allergenMaster(allergen_id):
#    children_id = session.get('children_id')
#   if children_id is None:
#       return redirect('/')

#    else:
#        allergen = dbConnect.getChildrenAllergens(children_id)
#        allergen.reverse()
#   return render_template('management/allergen.html', allergen_id=allergen_id, children_id=children_id)







if __name__ == '__main__':
    app.run (host= "0.0.0.0", debug = True)
