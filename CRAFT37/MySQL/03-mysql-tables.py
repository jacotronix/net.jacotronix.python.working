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
 
 
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table Created")
    except Error as e:
        print(e)
    c.close()
 
 
def main():
    sql_create_projects_table = """ CREATE TABLE projects (
                                        id integer NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
 
    sql_create_tasks_table = """CREATE TABLE tasks (
                                    id integer NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
 
    # create a database connection
    conn = create_connection()
 
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
 
        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

    conn.close()
 
 
if __name__ == '__main__':
    main()
