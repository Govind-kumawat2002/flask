import mysql.connector as mc
server=mc.connect(host ="13.60.207.151",
           user = "govind",
           password = "govind12345",
           database = 'boss')
cur=server.cursor()

querry = "select *from logine"
# insert into logine(user,password,values(%(user)s,%(password)s))

# cur.execute(querry)
# # print(cur.fetchone())
# print(cur.fetchall())
cur.close()
server.close()
