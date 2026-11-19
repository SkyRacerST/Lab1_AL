#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# TODO здесь заполнение словаря
def calculate_distances():
    distances = {}
    cities = list(sites.keys())
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i == j:
                continue
            city_a = cities[i]
            city_b = cities[j]
            x1, y1 = sites[city_a]
            x2, y2 = sites[city_b]
            distances[f'{city_a}-{city_b}'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distances

def run():     
    print(calculate_distances())

if __name__ == '__main__':
    run()