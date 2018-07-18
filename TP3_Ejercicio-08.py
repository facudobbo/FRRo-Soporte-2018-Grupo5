import pymysql
import datetime
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()
id=1
fecha= datetime.date(2018,3,14)
peso=60
cur.execute('SELECT idpersona from persona')
esta=False
for i in cur:
    if i[0]==id:
        esta=True

if not esta:
    print('No existe persona')
else:
    cur.execute('SELECT idpersona, max(fecha), peso FROM personapeso where idpersona=%s', id)
    for i in cur:
        if i[1] > fecha:
            print('Existe una fecha posterior')
        else:
            cur.execute('INSERT INTO personapeso(idpersona, fecha, peso) VALUES (%s,%s,%s)', (id, fecha, peso))
            conn.commit()
