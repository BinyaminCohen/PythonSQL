import sqlite3


def create_connection():
    conn = sqlite3.connect('student_database.db')
    return conn


def create_table(conn):
    cursor = conn.cursor()
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS student (
        fname TEXT,
        lname TEXT,
        score INT
    );
    """
    cursor.execute(create_table_sql)
    conn.commit()


def show_all_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    if students:
        for student in students:
            print(f"First Name: {student[0]}, Last Name: {student[1]}, Score: {student[2]}")
    else:
        print("There are no students.")


def add_new_student(conn):
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    score = input("Enter final score: ")

    cursor = conn.cursor()
    cursor.execute("INSERT INTO student (fname, lname, score) VALUES (?, ?, ?)",
                   (fname, lname, score))
    conn.commit()
    print("Student add successfully.")


def show_by_score(conn):
    score = input("Enter score: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student WHERE score >= ?", (score,))
    students = cursor.fetchall()
    for student in students:
        print(f"First Name: {student[0]}, Last Name: {student[1]}, Score: {student[2]}")


def main():
    conn = create_connection()
    create_table(conn)
    while True:
        print("\nMenu")
        print("1. Show all students")
        print("2. Add a new student")
        print("3. Show by score")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_all_students(conn)
        elif choice == '2':
            add_new_student(conn)
        elif choice == '3':
            show_by_score(conn)
        elif choice == '4':
            print("Quitting program")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == '__main__':
    main()
