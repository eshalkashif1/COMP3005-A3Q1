import os
import psycopg2
from dotenv import load_dotenv
import re
from datetime import datetime

# load environment variables from .env
load_dotenv()

# connect to DB
def connect_db():
    return psycopg2.connect(
        host=os.environ["PGHOST"],
        database=os.environ["PGDB"],
        user=os.environ["PGUSER"],
        password=os.environ["PGPASSWORD"],
        port=os.environ.get("PGPORT")
    )

# retrieve and display all students in DB
def getAllStudents():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM students ORDER BY student_id;"
            )
            students = cur.fetchall()

    if not students:
        print("No students found.")
        return
    
    for student in students:
        print(student)


# insert a new student into DB
def addStudent(first_name, last_name, email, enrollment_date):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO students
                    (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                RETURNING student_id;
                """,
                (first_name, last_name, email, enrollment_date)
            )
            student_id = cur.fetchone()[0]

    print(f"Student added successfully! ID: {student_id}")


# update email address of a student using their ID
def updateStudentEmail(student_id, new_email):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE students
                SET email = %s
                WHERE student_id = %s;
                """,
                (new_email, student_id)
            )
            updated = cur.rowcount

    if updated:
        print("Student email updated successfully!")
    else:
        print("Student not found.")


# delete a student from the database using their ID.
def deleteStudent(student_id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM students
                WHERE student_id = %s;
                """,
                (student_id,)
            )
            deleted = cur.rowcount

    if deleted:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# display menu for CRUD operations
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. View all students")
        print("2. Add a student")
        print("3. Update student email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == "1":
                getAllStudents()

            elif choice == "2":
                first_name = input("First name: ").strip()
                last_name = input("Last name: ").strip()
                email = input("Email: ").strip()
                date = input("Enrollment date (YYYY-MM-DD, optional): ").strip()

                # check names are not empty strings (in case user only enters a space)
                if not first_name or not last_name:
                    print("Error: First and last name cannot be empty.")
                    continue

                # check names do not contain numbers (validating format)
                if any(char.isdigit() for char in first_name + last_name):
                    print("Error: Names cannot contain numbers.")
                    continue

                # check correct email format
                if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
                    print("Error: Invalid email format.")
                    continue

                # check valid date (cant be 2022-13-41 for example), empty date is allowed
                if date:
                    try:
                        datetime.strptime(date, "%Y-%m-%d")
                    except ValueError:
                        print("Error: Invalid date. Use YYYY-MM-DD.")
                        continue
                else:
                    date = None

                addStudent(first_name, last_name, email, date)

            elif choice == "3":
                student_id = int(input("Student ID: "))
                new_email = input("New email: ")

                updateStudentEmail(student_id, new_email)

            elif choice == "4":
                student_id = int(input("Student ID: "))
                deleteStudent(student_id)

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1-5.")

        except (ValueError, psycopg2.Error) as error:
            print(f"Operation failed: {error}")


# start app
if __name__ == "__main__":
    main()


