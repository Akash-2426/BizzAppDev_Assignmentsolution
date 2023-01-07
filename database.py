#5. Provide a program to create tables (Employee Project) in database Sqlite and insert the data.
# import sqlite3
#
# from sqlite3 import Error
#
#
# def sql_connection():
#   try:
#     conn = sqlite3.connect('Employee.db')
#     return conn
#   except Error:
#     print(Error)
#
#
# def sql_table(conn):
#   cursorObj = conn.cursor()
#   cursorObj.execute("CREATE TABLE employee(employee_id n(5), ename char(30), ecity char(35), salary n(7));")
#   cursorObj.executescript("""
#    INSERT INTO employee VALUES(5001,'Akshay', 'New Mumbai', 15000);
#    INSERT INTO employee VALUES(5002,'Ronit', 'Pune', 32525);
#    INSERT INTO employee VALUES(5003,'Prashant', 'Panvel', 25000);
#    INSERT INTO employee VALUES(5004,'Pratik', 'Pen', 35000);
#    INSERT INTO employee VALUES(5005,'Prathmesh', 'Karjat', 22450);
#    """)
#   conn.commit()
#   cursorObj.execute("SELECT * FROM employee")
#   rows = cursorObj.fetchall()
#   print("Emp details:")
#   for row in rows:
#     print(row)
#
#
# sqllite_conn = sql_connection()
# sql_table(sqllite_conn)
# if (sqllite_conn):
#   sqllite_conn.close()
#   print("\nThe SQLite connection is closed.")


# 5. Provide a program to create tables (Department,Project) in database Sqlite and insert the data.

# import sqlite3
#
# from sqlite3 import Error
#
#
# def sql_connection():
#   try:
#     conn = sqlite3.connect('Department.db')
#     return conn
#   except Error:
#     print(Error)
#
#
# def sql_table(conn):
#   cursorObj = conn.cursor()
#   cursorObj.execute("CREATE TABLE department(dep_id n(5), dname char(30));")
#
#   cursorObj.executescript("""
#    INSERT INTO department VALUES(001,'Production');
#    INSERT INTO department VALUES(002,'Maintenance');
#    INSERT INTO department VALUES(003,'Quality');
#    INSERT INTO department VALUES(004,'Operation');
#    INSERT INTO department VALUES(005,'IT');
#    """)
#   conn.commit()
#   cursorObj.execute("SELECT * FROM department")
#   rows = cursorObj.fetchall()
#   print("Dept details:")
#   for row in rows:
#     print(row)
#
#
# sqllite_conn = sql_connection()
# sql_table(sqllite_conn)
# if (sqllite_conn):
#   sqllite_conn.close()
#   print("\nThe SQLite connection is closed.")

