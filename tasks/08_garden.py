#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# Создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
def garden_analysis():
	garden_set = set(garden)
	meadow_set = set(meadow)
	return f"{garden_set | meadow_set}\n{garden_set & meadow_set}\n{garden_set - meadow_set}\n{meadow_set - garden_set}"

def main():
    print(garden_analysis())


if __name__ == '__main__':
    main()