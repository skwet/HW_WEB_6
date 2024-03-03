from datetime import datetime
from faker import Faker
from connect import database,create_connection
import random
import sqlite3


groups = ['КБ-21','КБ-22','КБ-23']
subjects = ['Алгебра','Фізика','Англійська мова','Хімія','Фізкультура']

fake = Faker('uk_UA')

def fill_students(connect):
    cur = connect.cursor()
    for _ in range(30):
        name = fake.name()
        group_id = random.randint(1,3)
        cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))
        connect.commit()

def fill_groups(connect):
    cur = connect.cursor()
    for group in groups:
        cur.execute("INSERT INTO groups (name) VALUES (?)", (group,))
        connect.commit()

def fill_teachers(connect):
    cur = connect.cursor()
    for _ in range(5):
        name = fake.name()
        cur.execute("INSERT INTO teachers (name) VALUES (?)", (name,))
        connect.commit()

def fill_subjects(connect):
    cur = connect.cursor()
    for subject in subjects:
        teacher_id = random.randint(1,5)
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))
        connect.commit()

def fill_journal(connect):
    cur = connect.cursor()
    for student_id in range(1, 31):  
        for subject_id in range(1, 6): 
            for _ in range(random.randint(1, 20)):
                grade = random.randint(1, 5)
                date = fake.date_between(start_date="-1y", end_date="today")
                cur.execute("INSERT INTO journal (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)", (student_id, subject_id, grade, date))
                connect.commit()

if __name__ == '__main__':
    with create_connection(database) as conn:
        if conn is not None:
            fill_students(conn)
            fill_groups(conn)
            fill_teachers(conn)
            fill_subjects(conn)
            fill_journal(conn)
        else:
            print('Oops.. error occured!')