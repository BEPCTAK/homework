import numpy as np
import requests
import matplotlib.pyplot as plt

# Создание массива чисел
array = np.array([1, 2, 3, 4, 5])
print("Исходный массив:")
print(array)

# 1. Сложение массива с константой
added_array = array + 10
print("\nМассив после сложения с 10:")
print(added_array)

# 2. Умножение массива на константу
multiplied_array = array * 2
print("\nМассив после умножения на 2:")
print(multiplied_array)

# 3. Вычисление среднего значения массива
mean_value = np.mean(array)
print("\nСреднее значение массива:")
print(mean_value)

# 4. Вычисление стандартного отклонения
std_deviation = np.std(array)
print("\nСтандартное отклонение массива:")
print(std_deviation)

# 5. Применение функции к каждому элементу массива (квадрат)
squared_array = np.square(array)
print("\nМассив после возведения в квадрат:")
print(squared_array)

print("\n")

# Генерация данных
x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
y1 = np.sin(x)  # Синус
y2 = np.cos(x)  # Косинус
y3 = np.tan(x)  # Тангенс (с ограничением)

# Ограничение значений тангенса для лучшей визуализации
y3 = np.where(np.abs(y3) > 10, np.nan, y3)

# 1. Линейный график для синуса и косинуса
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)  # Создание подграфика (2 строки, 1 столбец, первый график)
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='orange')
plt.title('Графики синуса и косинуса')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Линия y=0
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Линия x=0
plt.legend()
plt.grid()

# 2. График тангенса
plt.subplot(2, 1, 2)  # Второй график в том же окне
plt.plot(x, y3, label='tan(x)', color='green')
plt.title('График тангенса')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Линия y=0
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Линия x=0
plt.ylim(-10, 10)  # Ограничение по оси y для лучшей визуализации
plt.legend()
plt.grid()

# Показать все графики
plt.tight_layout()  # Автоматическая настройка расположения графиков
plt.show()


# Функция для выполнения GET-запроса
def fetch_page(url):
    try:
        response = requests.get(url)  # Отправка GET-запроса
        response.raise_for_status()  # Проверка на наличие ошибок
        return response.text  # Возврат текста страницы
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)


# Функция для вывода данных
def print_page_content(content):
    print(content[:1000])  # Вывод первых 1000 символов страницы


# Основная функция для получения и отображения содержимого страницы
def main():
    url = 'https://ria.ru'  # URL для запроса
    page_content = fetch_page(url)  # Получение содержимого страницы
    if page_content:
        print_page_content(page_content)  # Вывод содержимого на консоль


# Запуск основной функции
if __name__ == "__main__":
    main()
