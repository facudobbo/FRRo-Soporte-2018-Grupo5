
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()
cur.execute("SELECT * FROM persona")


for fila in cur.fetchall():
    print('{0}, {1}, {2}, {3}, {4}'.format(fila[0], fila[1], fila[2], fila[3], fila[4]))


conn.close()
