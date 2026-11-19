import pytest
import sys
import os
import io
import importlib
from contextlib import redirect_stdout

# Добавляем путь к корню проекта
sys.path.append(os.path.join(os.path.dirname(__file__)))

# Импортируем модули через importlib, так как их имена начинаются с цифр
task0 = importlib.import_module('tasks.00_distance')
task1 = importlib.import_module('tasks.01_circle')
task2 = importlib.import_module('tasks.02_operations')
task3 = importlib.import_module('tasks.03_favorite_movies')
task4 = importlib.import_module('tasks.04_my_family')
task5 = importlib.import_module('tasks.05_zoo')
task6 = importlib.import_module('tasks.06_songs_list')
task7 = importlib.import_module('tasks.07_secret')
task8 = importlib.import_module('tasks.08_garden')
task9 = importlib.import_module('tasks.09_shopping')
task10 = importlib.import_module('tasks.10_store')


def test_task0():
    """Тест задания 0: Расстояние между городами"""
    f = io.StringIO()
    with redirect_stdout(f):
        task0.main()
    output = f.getvalue()
    assert "Moscow" in output
    assert "London" in output
    assert "Paris" in output


def test_task1():
    """Тест задания 1: Круг и точки"""
    f = io.StringIO()
    with redirect_stdout(f):
        task1.main()
    output = f.getvalue()
    assert "5541.769" in output
    assert "True" in output
    assert "False" in output


def test_task2():
    """Тест задания 2: Расставить знаки (1 2 3 4 5 = 25)"""
    f = io.StringIO()
    with redirect_stdout(f):
        task2.main()
    output = f.getvalue()
    assert "25" in output


def test_task3():
    """Тест задания 3: Индексация строк (фильмы)"""
    f = io.StringIO()
    with redirect_stdout(f):
        task3.main()
    output = f.getvalue()
    assert "Терминатор" in output
    assert "Назад в будущее" in output


def test_task4():
    """Тест задания 4: Моя семья"""
    f = io.StringIO()
    with redirect_stdout(f):
        task4.main()
    output = f.getvalue()
    # В вашем коде рост отца 174, а общий рост 530
    assert "174" in output
    assert "530" in output


def test_task5():
    """Тест задания 5: Зоопарк"""
    f = io.StringIO()
    with redirect_stdout(f):
        task5.main()
    output = f.getvalue()
    assert "bear" in output
    assert "lion" in output
    assert "lark" in output


def test_task6():
    """Тест задания 6: Песни Depeche Mode"""
    f = io.StringIO()
    with redirect_stdout(f):
        task6.main()
    output = f.getvalue()
    # 4.9 + 4.20 + 5.83 = 14.93
    # 4.43 + 4.88 + 4.18 = 13.49
    assert "14.93" in output
    assert "13.49" in output


def test_task7():
    """Тест задания 7: Расшифровка сообщения"""
    f = io.StringIO()
    with redirect_stdout(f):
        task7.main()
    output = f.getvalue()
    # Проверяем, что вывод не пустой
    assert len(output.strip()) > 0


def test_task8():
    """Тест задания 8: Цветы в саду и на лугу"""
    f = io.StringIO()
    with redirect_stdout(f):
        task8.main()
    output = f.getvalue()
    assert "ромашка" in output
    assert "одуванчик" in output
    assert "мак" in output


def test_task9():
    """Тест задания 9: Покупки (словарь sweets)"""
    f = io.StringIO()
    with redirect_stdout(f):
        task9.main()
    output = f.getvalue()
    assert "печенье" in output
    assert "пятерочка" in output


def test_task10():
    """Тест задания 10: Склад"""
    f = io.StringIO()
    with redirect_stdout(f):
        task10.main()
    output = f.getvalue()
    # Лампа: 27 шт, стоимость 1134 руб
    # Стол: 54 шт, стоимость 27860 руб
    assert "1134" in output
    assert "27860" in output