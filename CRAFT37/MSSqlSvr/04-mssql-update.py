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

 
def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
 
 
def main():
    # create a database connection
    conn = create_connection()
    update_task(conn, (2, '2015-01-04', '2015-01-06', 2))
 
 
if __name__ == '__main__':
    main()
