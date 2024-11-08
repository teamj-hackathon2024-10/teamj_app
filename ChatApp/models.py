import pymysql
from flask import abort
from util.DB import DB


class dbConnect:
  def createUSer(uid,name,email,password,phone_number,child_name,sex,allegeies,class_id,birthday,allegies_PDF=None):
    try:
        conn = DB.getConnection()
        cur = conn.cursor()
        user_sql = "INSERT INTO users (id, name, email, password, phone_number, admin) VALUES (%s, %s, %s, %s, %s, %s);"
        cur.execute(user_sql, (uid, name, email, password, phone_number,False))
        children_sql = "INSERT INTO children (user_id, name, sex, allegeies,class_id,birthday,allergies_pdf) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cur.execute(children_sql, (uid, child_name, sex, allegeies, class_id,birthday, allegies_PDF ))
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
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close


    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            cur.close()
            conn.close
