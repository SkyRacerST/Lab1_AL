#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
# sweets = {
#     'печенье': [
#         {'shop': 'пятерочка', 'price': 9.99},
#         {'shop': 'ашан', 'price': 10.99},
#     ],
#     ...
# }
# Указать надо только по 2 магазина с минимальными ценами
def two_cheapest():
    # Собираем все предложения по каждому продукту
    all_offers = {}
    for shop_name, products in shops.items():
        for product in products:
            all_offers.setdefault(product['name'], []).append(
                {'shop': shop_name, 'price': product['price']}
            )

    # Оставляем по 2 минимальные цены
    sweets = {}
    for name, offers in all_offers.items():
        offers.sort(key=lambda x: x['price'])
        sweets[name] = offers[:2]
    return sweets

def main():
    print(two_cheapest())


if __name__ == '__main__':
    main()