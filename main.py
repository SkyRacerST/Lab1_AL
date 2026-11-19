#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Верхнеуровневый модуль лабораторной работы №1.
Консольный интерфейс: выбор задания из меню.
"""

import os
import sys
import importlib

# Гарантируем, что корень проекта в sys.path,
# даже если main.py запускают из другой директории.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# Карта: номер задания -> (имя модуля, описание)
TASKS = {
    '0':  ('tasks.00_distance',        'Расстояния между городами'),
    '1':  ('tasks.01_circle',          'Площадь круга и точки'),
    '2':  ('tasks.02_operations',      'Получить 25 из 1 2 3 4 5'),
    '3':  ('tasks.03_favorite_movies', 'Любимые фильмы (срезы)'),
    '4':  ('tasks.04_my_family',       'Рост членов семьи'),
    '5':  ('tasks.05_zoo',             'Зоопарк'),
    '6':  ('tasks.06_songs_list',      'Песни Depeche Mode'),
    '7':  ('tasks.07_secret',          'Расшифровка секретного сообщения'),
    '8':  ('tasks.08_garden',          'Цветы в саду и на лугу'),
    '9':  ('tasks.09_shopping',        'Самые дешёвые магазины'),
    '10': ('tasks.10_store',           'Отчёт по складу'),
}


def show_menu():
    print('\n' + '=' * 55)
    print('  Лабораторная работа №1 — Введение в Python')
    print('=' * 55)
    for num, (_, description) in TASKS.items():
        print(f'  {num:>2}. {description}')
    print('   q. Выход')
    print('=' * 55)


def run_task(number):
    if number not in TASKS:
        print(f'[!] Нет задания с номером {number}')
        return

    module_name, description = TASKS[number]
    print(f'\n>>> Задание {number}: {description}')
    print('-' * 55)

    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        print(f'[!] Не удалось импортировать {module_name}: {e}')
        return

    if hasattr(module, 'main'):
        module.main()
    else:
        print(f'[!] В модуле {module_name} нет функции run()')


def main():
    while True:
        show_menu()
        choice = input('Выберите задание (0-10 или q): ').strip().lower()

        if choice in ('q', 'quit', 'exit', 'выход'):
            print('До встречи!')
            break

        run_task(choice)
        input('\nНажмите Enter, чтобы вернуться в меню...')


if __name__ == '__main__':
    main()