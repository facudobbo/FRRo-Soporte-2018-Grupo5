
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()

caux= "INSERT INTO persona(idpersona, nombre, fecha_nacimiento, dni, altura) VALUES (%s,%s,%s,%s,%s)"

tdatos=(6, 'Maria', '19960926', '40578554', '170')

cur.execute(caux,tdatos)
conn.commit()
