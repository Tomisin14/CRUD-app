import sqlite3

def create_connection():
    conn = sqlite3.connect('students.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
import sqlite3


def create_connection():
    return sqlite3.connect('students.db')


def create_student(name, age, grade):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
     INSERT INTO students (name, age, grade)
     VALUES (?, ?, ?)
     ''', (name, age, grade))
    conn.commit()
    conn.close()


def read_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_student(student_id, name, age, grade):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
     UPDATE students
     SET name = ?, age = ?, grade = ?
     WHERE id = ?
     ''', (name, age, grade, student_id))
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()


def display_students():
    students = read_students()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")


def main():
    while True:
        print("\nStudent Registration System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            create_student(name, age, grade)
            print("Student added successfully!")
        elif choice == '2':
            print("Student List:")
            display_students()
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new student name: ")
            age = int(input("Enter new student age: "))
            grade = input("Enter new student grade: ")
            update_student(student_id, name, age, grade)
            print("Student updated successfully!")
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
            print("Student deleted successfully!")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
