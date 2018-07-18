import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()

cur.execute("DELETE FROM persona WHERE idpersona = %s", 6)

conn.commit()
