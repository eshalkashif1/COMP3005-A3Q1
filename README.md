# COMP 3005 - Assignment 3

## Student Management System

This project is a Python application that connects to a PostgreSQL database to perform CRUD (Create, Read, Update, Delete) operations on student records.

## Video Demonstration

PASTE LINK HERE

The video demonstrates database setup and all four CRUD operations, including verification in pgAdmin.

## Technologies Used

- Python 3
- PostgreSQL
- pgAdmin 4
- psycopg2

## Database Schema

The `students` table contains the following fields:

| Column | Type | Constraints |
|---|---|---|
| student_id | INTEGER | Primary Key, Auto-increment |
| first_name | TEXT | NOT NULL |
| last_name | TEXT | NOT NULL |
| email | TEXT | NOT NULL, UNIQUE |
| enrollment_date | DATE | Optional |

## Application Functions

1. **getAllStudents()**: Retrieves and displays all student records.
2. **addStudent()**: Inserts a new student record.
3. **updateStudentEmail()**: Updates a student's email using their ID.
4. **deleteStudent()**: Deletes a student record using their ID.

## Setup Instructions

### 1. Prerequisites

Install Python 3, PostgreSQL, and pgAdmin 4.

### 2. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd COMP3005-Assignment3
```

### 3. Create the Database

1. Open pgAdmin.
2. Create a database named `assignment3_db`.
3. Open the Query Tool for this database.
4. Execute the SQL scripts in `database/setup.sql` (create_table.sql first, then insert.sql).

This creates the `students` table and inserts the three required initial records.

### 4. Install Dependencies

Create and activate a Python virtual environment.

Install the required library:

```bash
python -m pip install -r requirements.txt
```


### 5. Configure Database Connection

The application uses a `.env` file to store PostgreSQL connection credentials.

1. Copy the `.env.example` file and rename the copy to `.env`.
2. Open the `.env` file and update the values to match your local PostgreSQL configuration:

   ```env
   PGHOST=localhost
   PGDB=assignment3_db
   PGUSER=postgres
   PGPASSWORD=your_password
   PGPORT=5432
   ```

3. Replace `your_password` with your PostgreSQL password and ensure the database name matches the one you created.

The application automatically loads these variables from `.env` using `python-dotenv`, and this file is excluded from Git using .gitignore.


### 6. Run the Application

```bash
python application/main.py
```

Select an option from the menu to perform the desired CRUD operation.

## Testing

Each operation can be verified in pgAdmin using:

```sql
SELECT * FROM students ORDER BY student_id;
```
