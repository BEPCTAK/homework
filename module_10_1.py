import time
from time import sleep
import threading


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза в 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")


# Измерение времени выполнения функции
start_time = time.time()

# Вызов функции write_words с заданными аргументами
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f"Время выполнения функций: {end_time - start_time:.2f} секунд")

# Создание потоков для вызова функции
threads = []
args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

# Измерение времени выполнения потоков
start_time_threads = time.time()

for arg in args:
    thread = threading.Thread(target=write_words, args=arg)
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Время выполнения потоков: {end_time_threads - start_time_threads:.2f} секунд")
