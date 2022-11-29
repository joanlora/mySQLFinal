import mysql.connector as mc # Joan Jose Lora

conn = mc.connect(host = 'localhost',user ='root', password = 'Idkbro', db = 'menagerie')
c = conn.cursor() 

c.execute("SELECT * FROM pet;")
pd = c.fetchall()

for i in pd:
    print(i[0], i[4])