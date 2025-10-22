import sqlite3
from tabulate import tabulate

DATABASE = 'database.db'

def print_database():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()

    if not rows:
        print("No students in the database.")
        return

    data = []
    for row in rows:
        courses = row[3] if row[3] else ""
        data.append([row[0], row[1], row[2], courses])

    print(tabulate(data, headers=["ID", "Name", "Age", "Courses"], tablefmt="grid"))

if __name__ == '__main__':
    print_database()
