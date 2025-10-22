import sqlite3

DATABASE = 'database.db'

def get_all_students():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        students = []
        for row in rows:
            students.append({
                'id': row[0],
                'name': row[1],
                'age': row[2],
                'courses': row[3].split(",") if row[3] else []
            })
        return students
