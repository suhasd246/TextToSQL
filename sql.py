import sqlite3

##Connect to sqlite
connection = sqlite3.connect("student.db")

cursor = connection.cursor()
table_info = """
CREATE TABLE IF NOT EXISTS student ( NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

cursor.execute("INSERT INTO student (NAME, CLASS, SECTION, MARKS) VALUES ('John', 'CSE', 'A', 90)")
cursor.execute("INSERT INTO student (NAME, CLASS, SECTION, MARKS) VALUES ('Jane', 'ISE', 'B', 85)")
cursor.execute("INSERT INTO student (NAME, CLASS, SECTION, MARKS) VALUES ('Jim', 'ECE', 'C', 70)")
cursor.execute("INSERT INTO student (NAME, CLASS, SECTION, MARKS) VALUES ('Jill', 'ME', 'A', 65)")
cursor.execute("INSERT INTO student (NAME, CLASS, SECTION, MARKS) VALUES ('Jisdll', 'ME', 'A', 95)")
cursor.execute("INSERT INTO student (NAME, CLASS, SECTION, MARKS) VALUES ('Ram', 'ME', 'B', 95)")



print("Data inserted successfully")

data = cursor.execute("SELECT * FROM student")

for row in data:
    print(row)

connection.commit()
connection.close()

