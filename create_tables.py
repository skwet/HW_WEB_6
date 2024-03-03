from sqlite3 import Error
from connect import create_connection, database


def create_table(connect, create_table_sql):
    try:
        cur = connect.cursor()
        cur.execute(create_table_sql)
        connect.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_students_table = """
    CREATE TABLE students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups (id)
    );
    """

    sql_create_groups_table = """
    CREATE TABLE groups(
        id INTEGER PRIMARY KEY,
        name TEXT
    );
    """

    sql_create_teachers_table = """
    CREATE TABLE teachers(
        id INTEGER PRIMARY KEY,
        name TEXT,
    );
    """

    sql_create_subjects_table = """
    CREATE TABLE subjects(
        id INTEGER PRIMARY KEY,
        name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    );
    """

    sql_create_journal_table = """
    CREATE TABLE journal(
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date TEXT,
        FOREIGN KEY (student_id) REFERENCES students (id)
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
    );
    """
    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_create_students_table)
            create_table(conn, sql_create_groups_table)
            create_table(conn, sql_create_teachers_table)
            create_table(conn, sql_create_subjects_table)
            create_table(conn, sql_create_journal_table)
        else:
            print("Oops... error!")