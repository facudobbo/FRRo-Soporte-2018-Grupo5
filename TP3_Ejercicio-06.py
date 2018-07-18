import pymysql
import json
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()

cur.execute('SELECT idpersona, nombre, dni, altura FROM persona')

for fila in cur:
     print(json.dumps(fila))
