from flask import Flask, render_template, request, redirect
import sqlite3
import secrets
import string

app = Flask(__name__)


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_db_connection():

    connection = sqlite3.connect("students.db")

    connection.row_factory = sqlite3.Row

    return connection


# ==========================================
# CREATE DATABASE TABLE
# ==========================================

def create_table():

    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT NOT NULL,

            contact TEXT NOT NULL,

            enrollment TEXT NOT NULL UNIQUE,

            unique_key TEXT NOT NULL UNIQUE

        )
    """)

    connection.commit()

    connection.close()


# ==========================================
# GENERATE UNIQUE KEY
# ==========================================

def generate_unique_key():

    characters = string.ascii_uppercase + string.digits

    while True:

        key = ''.join(
            secrets.choice(characters)
            for _ in range(8)
        )

        connection = get_db_connection()

        existing_key = connection.execute(
            "SELECT id FROM students WHERE unique_key = ?",
            (key,)
        ).fetchone()

        connection.close()

        if existing_key is None:

            return key


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# REGISTRATION PAGE
# ==========================================

@app.route("/register")
def registration_page():

    return render_template("register.html")


# ==========================================
# REGISTER STUDENT
# ==========================================

@app.route("/register", methods=["POST"])
def register():

    # Get data from HTML form

    name = request.form["name"]

    email = request.form["email"]

    contact = request.form["contact"]

    enrollment = request.form["enrollment"]


    # Remove unnecessary spaces

    name = name.strip()

    email = email.strip()

    contact = contact.strip()

    enrollment = enrollment.strip()


    # Connect to database

    connection = get_db_connection()


    # Check whether enrollment already exists

    existing_student = connection.execute(
        "SELECT * FROM students WHERE enrollment = ?",
        (enrollment,)
    ).fetchone()


    if existing_student:

        connection.close()

        return render_template(
            "register.html",
            error="This enrollment number is already registered."
        )


    # Generate unique key

    unique_key = generate_unique_key()


    # Save student information

    connection.execute("""
        INSERT INTO students
        (name, email, contact, enrollment, unique_key)

        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        email,
        contact,
        enrollment,
        unique_key
    ))


    connection.commit()

    connection.close()


    # Show generated key

    return render_template(
        "register.html",
        success=True,
        unique_key=unique_key,
        student_name=name
    )


# ==========================================
# ENTER UNIQUE KEY PAGE
# ==========================================

@app.route("/enter-key")
def enter_key():

    return render_template("enter_key.html")


# ==========================================
# FIND STUDENT USING UNIQUE KEY
# ==========================================

@app.route("/find-student", methods=["POST"])
def find_student():

    # Get unique key from form

    unique_key = request.form["unique_key"]

    # Remove spaces and convert to uppercase

    unique_key = unique_key.strip().upper()


    # Connect to database

    connection = get_db_connection()


    # Search for student

    student = connection.execute(
        "SELECT * FROM students WHERE unique_key = ?",
        (unique_key,)
    ).fetchone()


    connection.close()


    # If key doesn't exist

    if student is None:

        return render_template(
            "enter_key.html",
            error="Invalid unique key."
        )


    # If key exists

    return render_template(
        "student_details.html",
        student=student
    )


# ==========================================
# ADMIN DASHBOARD
# ==========================================

@app.route("/admin")
def admin():

    connection = get_db_connection()


    # Get all students

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()


    connection.close()


    return render_template(
        "admin.html",
        students=students
    )


# ==========================================
# DELETE STUDENT
# ==========================================

@app.route("/delete-student/<int:student_id>", methods=["POST"])
def delete_student(student_id):

    connection = get_db_connection()


    # Delete student using unique database ID

    connection.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )


    connection.commit()

    connection.close()


    # Return to admin dashboard

    return redirect("/admin")


# ==========================================
# START APPLICATION
# ==========================================

if __name__ == "__main__":

    # Create database and table

    create_table()

    # Start Flask server

    app.run(debug=True)