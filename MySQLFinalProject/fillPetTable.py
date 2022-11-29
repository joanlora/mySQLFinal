import mysql.connector as mc # Joan Jose Lora

conn = mc.connect(host = 'localhost',user ='root', password = 'Idkbro', db = 'menagerie')
c = conn.cursor() 

c.execute("INSERT INTO pet (name,owner,species,sex,birth,death,age) VALUES \
    ('Fluffy','Harold', 'cat', 'f','1993-02-04',NULL,10),\
    ('Claws','Gwen', 'cat', 'm','1994-03-17',NULL,9),\
    ('Buffy','Harold', 'dog', 'f','1989-05-13',NULL,14),\
    ('Fang','Benny', 'dog', 'm','1990-08-27',NULL,12),\
    ('Bowser','Diane', 'dog', 'm','1979-08-31','1995-07-29',13),\
    ('Chripy','Gwen', 'bird', 'f','1998-09-11',NULL,4),\
    ('Whistler','Gwen', 'bird', 'NULL','1997-12-09',NULL,5),\
    ('Slim','Benny', 'snake', 'm','1996-04-29',NULL,7),\
    ('Puffball','Diane', 'hamster', 'f','1999-03-30',NULL,4)")

conn.commit()

print("Data has been loaded.")
