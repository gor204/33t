import sqlite3

# try:
#     connection = sqlite3.connect('sqlite.db')
# except sqlite3.DatabaseError:
#     print('При подключении к БД возникла ошибка')
# finally:
#     connection.close()


class User:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender


def create_users_table(cur: sqlite3.Cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    gender TEXT,
    age INTEGER,
    name TEXT)
    """
    cur.execute(command)


def add_new_user(cur: sqlite3.Cursor, user: User):
    command = """
    INSERT INTO users(name, age, gender) VALUES(?, ?, ?)
    """
    cur.execute(command, (user.name, user.age, user.gender))


def get_all_users(cur: sqlite3.Cursor):
    command = """
    SELECT * FROM users
    """
    result = cur.execute(command)
    return result.fetchall()


def update_user_name(cur: sqlite3.Cursor, user_id: int, name: str):
    command = """
    UPDATE users SET name = ? WHERE id = ?
    """
    cur.execute(command, (name, user_id))


def delete_all_users(cur: sqlite3.Cursor):
    command = """
    DELETE FROM users
    """
    cur.execute(command)


def get_user_by_id(cur: sqlite3.Cursor, user_id: int):
    command = """
    SELECT * FROM users WHERE id = ?
    """
    result = cur.execute(command, (user_id,))
    return result.fetchone()


# def delete_id_users(cur: sqlite3.Cursor):
#  command = """
# DELETE FROM USERS WHERE id = 2 LIMIT 1
# """
# cur.execute(command)

def get_employee_gender(cur: sqlite3.Cursor):
    command = """
    SELECT * FROM employees WHERE gender='male'
    """
    # return employee.fetchall()

    for res in cursor.fetchall():
        print(res)

    gender = input()
    if gender == 'М':
        print('Ваш пол: мужской!')
    elif gender == 'Ж':
        print('Ваш пол является женским!')

    else:
        print('Не знаю такой команды)')


if __name__ == '__main__':
    with sqlite3.connect('sqlite.db') as connection:
        cursor = connection.cursor()
        create_users_table(cursor)
        delete_all_users(cursor)
        user1 = User(name='Максим', age=16, gender='М')
        user2 = User(name='Ксения', age=15, gender='Ж')
        add_new_user(cursor, user1)
        add_new_user(cursor, user2)
        users = get_all_users(cursor)
        print(users)
        update_user_name(cursor, 2, 'Леша')
        users = get_all_users(cursor)
        print(users)
        lesha = get_user_by_id(cursor, 2)
        print(lesha)
        #  delete_id_users(cursor)
        employee = get_employee_gender(cursor)
