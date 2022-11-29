import mysql.connector as mc # Joan Jose Lora

conn = mc.connect(host = 'localhost',user ='root', password = 'Idkbro', db = 'menagerie')
c = conn.cursor() 

c.execute("DESCRIBE pet")
print(c.fetchall())
