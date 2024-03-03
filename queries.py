import sqlite3
from connect import create_connection,database

def reading_file(file_name):
    with open(file_name,'r') as file:
       res = file.read()
       return res
    
def db_query(connect,file_name):
    cur = connect.cursor()
    file_res = reading_file(file_name)
    cur.execute(file_res)
    db_res = cur.fetchall()
    return db_res

if __name__ == '__main__':
    number = int(input('Введіть число для запиту до БД: '))

    if number <= 10:
        file_name = f'db_queries/query_{number}.sql'
        file_res = reading_file(file_name)
    else:
        print(f'{number} немає в списку запитів. Введіть від 1 до 10!')
    
    with create_connection(database) as conn:
        if conn is not None:
            print('Результат:')
            print(db_query(conn,file_name))
        else:
            print('Oops... error!')
    





