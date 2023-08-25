""" Задача №3
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
"""
from itertools import combinations


def find_combinations(items, max_weight):
    valid_combinations = []
    for r in range(1, len(items) + 1):
        for combo in combinations(items.keys(), r):
            total_weight = sum(items[item] for item in combo)
            if total_weight <= max_weight:
                valid_combinations.append(combo)
    return valid_combinations


items = {
    "Тент": 3,
    "Спальник": 2,
    "Еда": 4,
    "Вода": 1,
    "Котелок": 2,
    "Фонарик": 1,
    "Топор": 3
}

max_weight = 5

valid_combinations = find_combinations(items, max_weight)

print(f"Грузоподъемность рюкзака: {max_weight} кг\n")
for i, combo in enumerate(valid_combinations, start=1):
    total_weight = sum(items[item] for item in combo)
    print(f"Вариант комплектации рюкзака {i}:")
    for item in combo:
        print(f"  {item} (Масса: {items[item]} кг)")
    print(f"  Общая масса: {total_weight} кг\n")
