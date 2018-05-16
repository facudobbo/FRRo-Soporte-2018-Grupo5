import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur=conn.cursor()

cur.execute(""" create table personaPeso
                    (
                        idPersona int, 
                        fecha date,
                        peso int,
                        primary key (idPersona, fecha),
                        index (idPersona),
                        foreign key (idPersona) references persona(idpersona)
                    )   
             """)

