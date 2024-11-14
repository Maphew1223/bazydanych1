# ex_03.py
import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful.")
    except sqlite3.Error as e:
        print(f"Error creating connection: {e}")
    return conn

def add_project(conn, project):
    sql = '''INSERT INTO projects(nazwa, start_date, end_date) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def add_task(conn, task):
    sql = '''INSERT INTO tasks(project_id, nazwa, opis, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def get_projects(conn):
    sql = '''SELECT * FROM projects'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

def update_task_status(conn):
    sql = '''UPDATE tasks SET status = 'ended' '''
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("All task statuses updated to 'ended'.")
    except sqlite3.Error as e:
        print(f"Error updating task statuses: {e}")

def delete_all_projects(conn):
    """Delete all rows in the projects table."""
    sql = 'DELETE FROM projects'
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("All projects deleted.")
    except sqlite3.Error as e:
        print(f"Error deleting projects: {e}")

def delete_all_tasks(conn):
    """Delete all rows in the tasks table."""
    sql = 'DELETE FROM tasks'
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("All tasks deleted.")
    except sqlite3.Error as e:
        print(f"Error deleting tasks: {e}")

if __name__ == "__main__":
    conn = create_connection("database.db")
    
    if conn:

        delete_all_tasks(conn)
        delete_all_projects(conn)

        conn.close()
        print("Connection closed.")
