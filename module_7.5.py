import os
import time

directory = "."  # Укажите директорию для обхода

for root, dirs, files in os.walk(directory):  # Обход каталога
    for file in files:
        filepath = os.path.join(root, file)  # Формирование полного пути к файлу
        filetime = os.path.getmtime(filepath)  # Получение времени последнего изменения файла

        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Форматирование времени

        filesize = os.path.getsize(filepath)  # Получение размера файла

        parent_dir = os.path.dirname(filepath)  # Получение родительской директории файла

        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}'
            f', Родительская директория: {parent_dir}')
