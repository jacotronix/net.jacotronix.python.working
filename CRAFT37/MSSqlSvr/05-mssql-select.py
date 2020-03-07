import pyodbc 
from pyodbc import Error
 
def create_connection():
    """ 
     :return: Connection object or None
    """
    conn = None
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DEVVM;'
                              'Database=pythonlearning;'
                              'Trusted_Connection=yes;')
        return conn
    except Error as e:
        print(e)
 
    return conn

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority, ))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def main():
    # create a database connection
    conn = create_connection()
    print("1. Query task by priority:")
    select_task_by_priority(conn, 1)
 
    print("2. Query all tasks")
    select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()

