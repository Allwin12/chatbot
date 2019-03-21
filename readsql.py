import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT text,occurrence FROM 'ResponseTable' order by occurrence desc LIMIT 5")
 
    rows = cur.fetchall()
    f=open("faq.txt","w")
    for row in rows:
        f.write(str(row))
        print(row)
    f.close()

        
def main():
    database = "C:\project\db.sqlite3"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("2. Query all tasks")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()
