import mysql.connector as mc # Joan Jose Lora

conn = mc.connect(host = 'localhost',user ='root', password = 'Idkbro')
c = conn.cursor()

c.execute('DROP DATABASE IF EXISTS menagerie')
print('Database has been dropped')