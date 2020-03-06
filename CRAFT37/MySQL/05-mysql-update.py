import mysql.connector
from mysql.connector import Error

def create_connection():
    """ 
     :return: Connection object or None
    """
    conn = None
    try:
        conn = mysql.connector.connect(host="localhost",
                                       user="jamie",
                                       passwd="mysqldb",
                                       database="pythonlearning")
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
              SET priority = %s ,
                  begin_date = %s ,
                  end_date = %s
              WHERE id = %s'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
 
 
def main():
    # create a database connection
    conn = create_connection()
    update_task(conn, (2, '2015-01-04', '2015-01-06', 4))
 
 
if __name__ == '__main__':
    main()
