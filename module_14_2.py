import sqlite3


conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполняем таблицу 10 записями
if cursor.execute("SELECT COUNT(*) FROM Users").fetchone()[0] == 0:
    users_data = [
        ('User1', 'example1@gmail.com', 10, 1000),
        ('User2', 'example2@gmail.com', 20, 1000),
        ('User3', 'example3@gmail.com', 30, 1000),
        ('User4', 'example4@gmail.com', 40, 1000),
        ('User5', 'example5@gmail.com', 50, 1000),
        ('User6', 'example6@gmail.com', 60, 1000),
        ('User7', 'example7@gmail.com', 70, 1000),
        ('User8', 'example8@gmail.com', 80, 1000),
        ('User9', 'example9@gmail.com', 90, 1000),
        ('User10', 'example10@gmail.com', 100, 1000)
    ]
    cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)

# Обновляем balance у каждой 2-й записи начиная с 1-й на 500
cursor.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1")

# Удаляем каждую 3-ю запись в таблице начиная с 1-й
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# Удаляем запись с id = 6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчитываем общее количество записей
total_users = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()[0]
print(f'Общее количество записей: {total_users}')

# Подсчитываем сумму всех балансов
all_balances = cursor.execute("SELECT SUM(balance) FROM Users").fetchone()[0]
print(f'Сумма всех балансов: {all_balances}')

# Вычисляем средний баланс
average_balance = all_balances / total_users if total_users > 0 else 0
print(f'Средний баланс всех пользователей: {average_balance:.2f}')

# Дополнительный вывод среднего баланса
print(all_balances / total_users if total_users > 0 else "Нет пользователей для расчета среднего баланса")

# Выборка всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()

# Выводим результаты в консоль
for username, email, age, balance in results:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')


conn.commit()
conn.close()
