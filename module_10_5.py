import time
from multiprocessing import Pool
import os


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


def linear_read(filenames):
    for filename in filenames:
        read_info(filename)


def parallel_read(filenames):
    with Pool() as pool:
        pool.map(read_info, filenames)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    for filename in filenames:
        if not os.path.exists(filename):
            print(f"Файл {filename} не найден.")
            exit(1)

    # Линейный вызов
    start_time = time.time()
    linear_read(filenames)
    linear_time = time.time() - start_time
    print(f"Время выполнения линейного вызова: {linear_time:.4f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    parallel_read(filenames)
    multiprocessing_time = time.time() - start_time
    print(f"Время выполнения многопроцессного вызова: {multiprocessing_time:.4f} секунд")
