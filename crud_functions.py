import sqlite3


def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Создание таблицы Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Создание таблицы Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    conn.commit()
    conn.close()


def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) 
        VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))

    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    conn.close()

    return user is not None

# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


def populate_db():
    products = [
        ('Product1', 'Описание продукта 1', 100),
        ('Product2', 'Описание продукта 2', 200),
        ('Product3', 'Описание продукта 3', 300),
        ('Product4', 'Описание продукта 4', 400),
    ]

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    initiate_db()
    populate_db()  # Заполнение базы данных