import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()
dni=input('Introduce DNI:')
cur.execute('SELECT * FROM persona WHERE dni=%s ', dni)
persona=cur.fetchone()
cur.execute('SELECT * FROM personapeso WHERE idpersona=%s ', persona[0])

print(persona[1],'\n',persona[2],'\n',persona[3],'\n', persona[4])
for i in cur.fetchall():
    print('Id:{0} \t Fecha:{1} \t Peso:{2}\n'.format(i[0],i[1],i[2]))
