import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()

cur.execute("SELECT * FROM persona WHERE dni= %s", 40317305)

fila=cur.fetchone()
print('Id:{0}\nNombre:{1}\nFecha Nacimiento:{2}\nDNI:{3}\nAltura:{4}'.format(fila[0],fila[1],fila[2],fila[3],fila[4]))
cur.close()
