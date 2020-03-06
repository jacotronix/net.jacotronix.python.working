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

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

    # Got to be a better way than this to get the id of the inserted row!  MySQL has cur.lastrowid!
    rows = cur.execute('''SELECT id FROM projects WHERE  ID = IDENT_CURRENT('projects')''')
    for row in rows:
        r = row[0]
    return r
 
 
def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return
 
 
def main():
    # create a database connection
    conn = create_connection()

    # create a new project
    project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
    project_id = create_project(conn, project)
 
    # tasks
    task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
    task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
 
    # create tasks
    create_task(conn, task_1)
    create_task(conn, task_2)
 
 
if __name__ == '__main__':
    main()

