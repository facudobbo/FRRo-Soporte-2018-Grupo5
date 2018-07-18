import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()

cur.execute("UPDATE persona SET altura=115 WHERE dni=%s ",40317305)

conn.commit()
