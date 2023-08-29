"""
Задача №1
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os


def get_file_info(file_path):
    path, file_name = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(file_name)
    return path, file_name, file_extension


absolute_path = r"C:\Users\IRINA\PycharmProjects\Homework\Homework_5"
result = get_file_info(absolute_path)
print(result)
