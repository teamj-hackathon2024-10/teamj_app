import pymysql
from flask import abort
from util.DB import DB


class dbConnect:
    def createUser(name,email,password,phone_number,child_name,sex,allergies,birthday,allergies_PDF=None):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            user_sql = "INSERT INTO users ( name, email_address, password, phone_number, admin) VALUES (%s, %s, %s, %s, %s);"
            cur.execute(user_sql, ( name, email, password, phone_number,0))
            user_id_sql = 'SELECT id FROM users WHERE email_address=%s'
            cur.execute(user_id_sql, (email))
            user_id = cur.fetchone()
            print(user_id)
            children_sql = "INSERT INTO children (user_id, name, sex, allergies,birthday,allergies_pdf) VALUES (%s, %s, %s, %s, %s, %s);"
            cur.execute(children_sql, (user_id['id'], child_name, sex, allergies, birthday, allergies_PDF ))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()



    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email_address=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()


    def addUserToChannel(user_id, channel_id):
        #ユーザーをチャンネルに追加する
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO userchannels (user_id, channel_id) VALUES (%s, %s);"
            cur.execute(sql, (user_id, channel_id ))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()


    def getUserChannels(user_id):
        #特定のユーザーを関連づけたチャンネルの取得
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = """SELECT * FROM userchannels AS U
            INNER JOIN channels AS C
            ON U.channel_id = C.id
              WHERE U.user_id = %s;"""
            cur.execute(sql, (user_id))
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()



    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()

    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()



    def updateChannel(uid, newChannelName, newChannelDescription, cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
            cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()


    def deleteChannel(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()


    def getMessageAll(channel_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT m.id, u.id, name, message FROM messages AS m INNER JOIN users AS u ON m.user_id = u.id WHERE channel_id = %s;"
            cur.execute(sql, (channel_id))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()


    def createMessage(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, message))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()
            conn.close()



