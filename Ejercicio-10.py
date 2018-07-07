import pymysql
import json
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()
cur2=conn.cursor()
cur.execute('SELECT idpersona, nombre, dni, altura FROM persona')



for i in cur:
    print(json.dumps(i))
    cur2.execute('SELECT idpersona, peso FROM personapeso where idpersona=%s', i[0])
    print(json.dumps(cur2.fetchall()))


