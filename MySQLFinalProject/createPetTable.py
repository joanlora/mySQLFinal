import mysql.connector as mc # Joan Lora

conn = mc.connect(host = 'localhost',user ='root', password = 'Idkbro', db = 'menagerie')
c = conn.cursor() 

def create_table():

    c.execute('DROP TABLE IF EXISTS pet')
    c.execute('CREATE TABLE pet \
            ( \
                name  VARCHAR(20), \
                owner VARCHAR(20), \
                species VARCHAR(20), \
                sex CHAR(10), \
                birth DATE, \
                death DATE, \
                age   int \
            )'
    )


def commit_close():
    """ commit changes to database and close connection """
    conn.commit()
    c.close()
    conn.close()

def main():
    """ execute create and insert commands """
    create_table()
    commit_close() 

if __name__ == '__main__':
    main()