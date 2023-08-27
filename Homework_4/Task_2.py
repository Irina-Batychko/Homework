""" Задача №2
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def get_arguments(**kwargs):
    arguments_dict = {}
    for arg_name, arg_value in kwargs.items():
        key = arg_value if hashable(arg_value) else str(arg_value)
        arguments_dict[key] = arg_name
    return arguments_dict


def hashable(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False


result = get_arguments(name='Irina', age=41, height=1.68, weight='62 kg')
print(result)
