"""
Задача №2
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.

Задача №1 из семинара №8
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
всех вложенных файлов и директорий.
"""

import os
import json
import csv
import pickle


class DirectoryInfo:
    def __init__(self, directory):
        self.directory = directory
        self.data = []

    def get_directory_info(self):
        for root, dirs, files in os.walk(self.directory):
            total_size = sum(
                os.path.getsize(os.path.join(root, file)) for file in files
            )

            dir_info = {
                'name': os.path.basename(root),
                'path': os.path.relpath(root, self.directory),
                'type': 'directory',
                'size': total_size,
            }

            self.data.append(dir_info)

            for file in files:
                file_info = {
                    'name': os.path.basename(file),
                    'path': os.path.relpath(root, self.directory),
                    'type': 'file',
                    'size': os.path.getsize(os.path.join(root, file)),
                }

                self.data.append(file_info)

    def save_results_as_json(self):
        with open('json_file_.json', 'w') as json_file:
            json.dump(self.data, json_file)

    def save_results_as_csv(self):
        with open('csv_file_.csv', 'w', newline='') as csv_file:
            fieldnames = ['name', 'path', 'type', 'size']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    def save_results_as_pickle(self):
        with open('pickle_file_.pickle', 'wb') as pickle_file:
            pickle.dump(self.data, pickle_file)


directory_info = DirectoryInfo(".")
directory_info.get_directory_info()
directory_info.save_results_as_json()
directory_info.save_results_as_csv()
directory_info.save_results_as_pickle()
