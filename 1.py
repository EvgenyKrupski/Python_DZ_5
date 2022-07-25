# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока,
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты
# оппонента достаются сделавшему последний ход. Сколько конфет
# нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""

from random import randint as rnd

def move(sweet, get):
    while True:
        player = int(input(f'Возьмите со стола конфеты не более {get}: '))
        if player <= get and player > 0:
            break
    if sweet-player < 0:
        print(f'Вы взяли оставшееся количество конфет со стола: {sweet}')
    else:
        print(f'Вы взяли количество конфет со стола: {player}')
    sweet -= player
    return sweet

candy = 2021
print(f'На столе лежат конфеты в количестве {candy}')
take = int(input('Определите максимально допустимое количество конфет за ход: '))
lot = 'ваш' if rnd(1, 2) == 1 else 'бота'
print(f'Жеребьёвка: Первый ход {lot}')

while candy > 0:
    if lot == 'ваш':
        rem = move(candy, take)
        candy = rem
        if candy <= 0:
            win = 'Игрок'
        print(f'Конфет на столе осталось: {candy}')

    bot = candy % (take+1)
    if candy-bot < 0:
        print(f'Бот взял оставшееся количество конфет со стола: {candy}')
    else:
        print(f'Бот взял количество конфет со стола: {bot}')
    candy -= bot
    if candy <= 0:
        win = 'Бот'
    print(f'Конфет на столе осталось: {candy}')

    if lot != 'ваш':
        rem = move(candy, take)
        candy = rem
        if candy <= 0:
            win = 'Игрок'
        print(f'Конфет на столе осталось: {candy}')

print(f'Победителем становится: {win}')