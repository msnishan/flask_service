import sqlite3


def load_data():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE Student
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT)''')
    cursor.execute("INSERT into Student VALUES(1, 'A', 34, 'A')")
    cursor.execute("INSERT into Student VALUES(4, 'B', 30, 'B')")
    cursor.execute("INSERT into Student VALUES(2, 'E', 15, 'E')")
    cursor.execute("INSERT into Student VALUES(3, 'D', 22, 'D')")
    connection.commit()
    connection.close()


def students_by_ids(ids):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from Student WHERE id in ({})".format(','.join('?' * len(ids))), ids)
    rows = cursor.fetchall()
    students = []
    for row in rows:
        students.append({
            'id': row[0],
            'name': row[1],
            'age': row[2],
            'grade': row[3]
        })
    return students
