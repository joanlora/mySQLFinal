import mysql.connector as mq

conn = mq.connect(host = 'localhost',user ='root', password = 'Idkbro',db = '') # connect to MySQL server

print("------MySQL Server Databases Joan Lora------")

c = conn.cursor()
sd = "show databases"
c.execute(sd) # executes the MySQL command for you
for (sd) in c:
    print (f"             {sd[0]}")

print("--------------------------------------------")