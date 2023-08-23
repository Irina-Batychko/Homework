""" Задача №1
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def convert_to_hexadecimal(number):
    hex_string = hex(number)[2:]
    return hex_string


number = int(input("Введите целое число: "))

hex_result = convert_to_hexadecimal(number)

print(f"Шестнадцатеричное представление: {hex_result}")

hex_builtin = hex(number)[2:]
print(f"Результат функции hex: {hex_builtin}")
