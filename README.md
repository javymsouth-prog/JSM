# JS Student Course Management

A small Flask-based student course management system. Use it to add, view, search, update, and delete student records stored in a local SQLite database (`database.db`).

## Features

- Add students with ID, name, age, and a selection of courses
- View all students in a table with actions to update or delete
- Search students by ID
- Update a student's selected courses
- Simple HTML templates with CSS styling

## Requirements

Python 3.10+ recommended.

Dependencies are listed in `requirements.txt` (Flask, tabulate, etc.).

## Quick setup (Windows PowerShell)

1. Open PowerShell and change to the project directory:

   ```powershell
   cd "C:\Users\User\Desktop\Database"
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Run the app:

   ```powershell
   python app.py
   ```

   The Flask dev server will start (default: http://127.0.0.1:5000). Open that URL in your browser.

## Files and structure

- `app.py` — Flask application and routes (index, add, view, search, update, delete).
- `student_db.py` — helper functions to read students from the SQLite DB.
- `check_database.py` — small CLI helper to print the DB using `tabulate`.
- `database.db` — SQLite database (created automatically if missing).
- `requirements.txt` — Python dependencies.
- `Templates/` — Jinja2 templates (`base.html`, `add.html`, `view.html`, `search.html`, `update.html`, `index.html`).
- `static/` — static files (CSS, images).
- `.vscode/launch.json` — optional VS Code launch configuration.

## Notes & Troubleshooting

- If the server fails to start, check that dependencies installed correctly and that no other process is using port 5000.
- To reset the database, stop the server and delete or rename `database.db`. Restart the app to recreate the table.
- If you use PowerShell execution policy errors when activating the venv, you can run:

  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

  Or activate using the `Activate.bat` script from cmd.exe:

  ```powershell
  .\.venv\Scripts\activate.bat
  ```