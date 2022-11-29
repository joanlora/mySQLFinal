import mysql.connector as mc # Joan Jose Lora
from tabulate import tabulate

conn = mc.connect(host = 'localhost',user ='root', password = 'Idkbro', db = 'menagerie')
c = conn.cursor() 

c.execute("SELECT name, birth, MONTH(birth) FROM pet;")
pd = c.fetchall()

print(tabulate(pd, headers= ['name','birth','MONTH(birth)'], tablefmt='psql'))
