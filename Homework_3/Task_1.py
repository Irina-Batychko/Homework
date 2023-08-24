""" Задача №1
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""


def remove_duplicates(input_list):
    unique_elements = set()
    result_list = []

    for item in input_list:
        if item not in unique_elements:
            unique_elements.add(item)
            result_list.append(item)

    return result_list


input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
result = remove_duplicates(input_list)
print(result)
