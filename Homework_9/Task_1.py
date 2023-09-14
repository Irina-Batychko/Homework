"""
Задача №1
Напишите следующие функции:
- Нахождение корней квадратного уравнения.
- Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
- Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
- Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""

import functools
import json
import math
import random
import csv


def quadratic_equation(a, b, c):
    # Функция для нахождения корней квадратного уравнения
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root1 = root2 = -b / (2 * a)
        return root1, root2
    else:
        return None


def get_csv_file(filename, num_rows):
    # Генерация csv файла с 3-мя случайными числами в каждой строке
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [random.randint(1, 100) for _ in range(3)]
            csv_writer.writerow(row)


def decorator_quadratic_equation(func):
    # Декоратор, запускающий функцию quadratic_equation для нахождения корней квадратного уравнения

    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                a, b, c = map(float, row)
                roots = func(a, b, c)
                print(f"Корни для a={a}, b={b}, c={c}: {roots}")

    return wrapper


def json_file_(filename):
    def decorator(func):
        # Декоратор для сохранения параметров и результатов функции в JSON файл
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "args": args,
                "result": result
            }
            with open(filename, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            return result

        return wrapper

    return decorator


@decorator_quadratic_equation
@json_file_("results.json")
def find_quadratic_roots(a, b, c):
    return quadratic_equation(a, b, c)


get_csv_file("random_numbers.csv", 100)
find_quadratic_roots("random_numbers.csv")
