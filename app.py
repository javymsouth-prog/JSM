from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret"

from student_db import get_all_students

DATABASE = 'database.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                courses TEXT
            )
        ''')
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        id_input = request.form['id']
        name = request.form['name']
        age = request.form['age']
        courses = request.form.getlist('courses')
        course_str = ",".join(courses)

        # Validate that ID is integer
        try:
            student_id = int(id_input)
        except ValueError:
            flash("Student ID must be an integer!", "danger")
            return redirect(url_for('add_student'))

        # Validate that Age is integer
        try:
            student_age = int(age)
        except ValueError:
            flash("Age must be an integer!", "danger")
            return redirect(url_for('add_student'))

        try:
            with sqlite3.connect(DATABASE) as conn:
                conn.execute("INSERT INTO students (id, name, age, courses) VALUES (?, ?, ?, ?)",
                             (student_id, name, student_age, course_str))
                flash("Student added successfully!", "success")
        except sqlite3.IntegrityError:
            flash("Student ID already exists!", "danger")

        return redirect(url_for('add_student'))
    return render_template('add.html')

@app.route('/view')
def view_students():
    students_dicts = get_all_students()
    return render_template('view.html', students=students_dicts)

@app.route('/search', methods=['GET', 'POST'])
def search_student():
    student = None
    if request.method == 'POST':
        id_input = request.form['id']

        # Validate integer ID
        try:
            student_id = int(id_input)
        except ValueError:
            flash("Student ID must be an integer!", "danger")
            return redirect(url_for('search_student'))

        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
            s = cur.fetchone()
            if s:
                student = {
                    'id': s[0],
                    'name': s[1],
                    'age': s[2],
                    'courses': s[3].split(",") if s[3] else []
                }
            else:
                flash("Student not found!", "warning")
    return render_template('search.html', student=student)

@app.route('/update/<id>', methods=['GET', 'POST'])
def update_student(id):
    # Ensure ID is integer
    try:
        student_id = int(id)
    except ValueError:
        flash("Invalid student ID!", "danger")
        return redirect(url_for('view_students'))

    if request.method == 'POST':
        courses = request.form.getlist('courses')
        course_str = ",".join(courses)
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("UPDATE students SET courses = ? WHERE id = ?", (course_str, student_id))
            flash("Courses updated successfully!", "success")
        return redirect(url_for('view_students'))

    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        s = cur.fetchone()
        if not s:
            flash("Student not found!", "warning")
            return redirect(url_for('view_students'))
        student = {
            'id': s[0],
            'name': s[1],
            'age': s[2],
            'courses': s[3].split(",") if s[3] else []
        }
    return render_template('update.html', student=student)

@app.route('/delete/<id>')
def delete_student(id):
    try:
        student_id = int(id)
    except ValueError:
        flash("Invalid student ID!", "danger")
        return redirect(url_for('view_students'))

    with sqlite3.connect(DATABASE) as conn:
        conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        flash("Student deleted successfully!", "info")
    return redirect(url_for('view_students'))

if __name__ == '__main__':
    app.run(debug=True)
