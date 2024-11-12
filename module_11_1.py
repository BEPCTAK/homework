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


# Функция для выполнения GET-запроса к Википедии
def fetch_wikipedia_homepage():
    url = "https://ru.wikipedia.org"
    response = requests.get(url)

    if response.status_code == 200:
        print("Данные успешно получены с Википедии:")
        print(response.text[:1000])  # Выводим первые 1000 символов текста
    else:
        print(f"Ошибка при получении данных: {response.status_code}")


print('\n')


# Функция для получения заголовков страницы
def fetch_headers(url):
    response = requests.head(url)

    if response.status_code == 200:
        print("Заголовки ответа:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    else:
        print(f"Ошибка при получении заголовков: {response.status_code}")


# Функция для выполнения POST-запроса (пример, хотя для Википедии это может быть неуместно)
def post_example():
    url = "https://httpbin.org/post"  # Используем httpbin для демонстрации POST-запроса
    data = {"key": "value"}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Данные успешно отправлены:")
        print(response.json())  # Выводим ответ в формате JSON
    else:
        print(f"Ошибка при отправке данных: {response.status_code}")


# Пример использования функций
if __name__ == "__main__":
    fetch_wikipedia_homepage()
    fetch_headers("https://ru.wikipedia.org")
    post_example()

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
