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
            cur.execute(user_id_sql, (email,))
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
            cur.execute(sql, (email,))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()


    def getAllUsers():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users;"
            cur.execute(sql)
            users = cur.fetchall()
            return users
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()




    # def addUserToChannel(user_id, channel_id):
    #     #ユーザーをチャンネルに追加する
    #     try:
    #         conn = DB.getConnection()
    #         cur = conn.cursor()
    #         sql = "INSERT INTO channels (user_id, channel_id) VALUES (%s, %s);"
    #         cur.execute(sql, (user_id, channel_id ))
    #         conn.commit()
    #     except Exception as e:
    #         print(f'エラーが発生しています：{e}')
    #         abort(500)
    #     finally:
    #         cur.close()
    #         conn.close()


    def getChannels(user_id):
        #個別チャンネルとオープンのチャンネルの情報
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = """SELECT * FROM channels
            WHERE is_open = TRUE
            OR user_id = %s
            ORDER BY update_at DESC;"""
            cur.execute(sql, (user_id,))
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()

    def getAdminChannels():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = """SELECT * FROM channels;"""
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()


    def getChannelMembers(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = """SELECT * FROM users
            INNER JOIN channels
            ON channels.user_id = users.id
            WHERE channels.channel_id = %s"""
            cur.execute(sql, (cid,))
            users = cur.fetchall()
            return users
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()

    def addChannel(channel_id, channel_name, is_open = False):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels (id, name, update_at, is_open) VALUES (%s, %s, NOW(), %s);"
            cur.execute(sql, (channel_id, channel_name, is_open))
            conn.commit()
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
            cur.execute(sql, (cid,))
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
            print(channel_name)
            sql = "SELECT * FROM channels WHERE name = %s;"
            print(channel_name)
            cur.execute(sql, (channel_name,))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()



    def updateChannel(channel_id, user_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE channels SET user_id= %s, update_at=NOW() WHERE id=%s;"
            cur.execute(sql, (user_id, channel_id))
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
            cur.execute(sql, (cid,))
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
            sql = """
            SELECT m.id AS message_id, u.id AS user_id, u.name AS user_name,
                   m.message, m.datetime
            FROM messages AS m
            INNER JOIN users AS u
            ON m.user_id = u.id
            WHERE m.channel_id = %s
            ORDER BY m.datetime ASC;
            """
            cur.execute(sql, (channel_id,))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()


    def createMessage(user_id, channel_id, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(user_id, channel_id, message, datetime) VALUES(%s, %s, %s, NOW())"
            cur.execute(sql, (user_id, channel_id, message))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()




    def getChildrenNameByUserId(user_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT name FROM children WHERE user_id=%s;"
            cur.execute(sql, (user_id,))
            child_name = cur.fetchall()
            return child_name
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close()
