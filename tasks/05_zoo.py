#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def build_zoo():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    zoo.insert(1, 'bear')

    birds = ['rooster', 'ostrich', 'lark']
    zoo.extend(birds)

    zoo.remove('elephant')

    lion_cell = zoo.index('lion') + 1
    lark_cell = zoo.index('lark') + 1
    return zoo, lion_cell, lark_cell


def main():
    zoo, lion, lark = build_zoo()
    print(zoo)
    print(f"Лев сидит в клетке {lion}")
    print(f"Жаворонок сидит в клетке {lark}")


if __name__ == '__main__':
    main()