import random
from repl import calculate_change

sorts = {1: {'name': 'эспрессо', 'price': 150},
         2: {'name': 'американо', 'price': 200},
         3: {'name': 'капуччино', 'price': 250},
         4: {'name': 'латте', 'price': 350},
         5: {'name': 'ристретто', 'price': 300},
         6: {'name': 'доппио', 'price': 350},
         7: {'name': 'молоко', 'price': 50}}


with open('slogans.txt') as f:
    slogans = f.read().split(';')


def main():
    while True:
        random_number = random.randrange(1, 19)
        print(f'''Добро пожаловать в кофейню - "{slogans[random_number]}!"      
Найдите Ваш напиток:''')
        for i in sorts.keys():
            print(f"{i}.{sorts[i]['name']} - {sorts[1]['price']} руб;")
        print('Введите 0 для завершения')
        command = int(input('Введите номер:   '))
        if command == 0:
            break
        print(calculate_change(sorts[command]['price'], sorts[command]['name']))


if __name__ == "__main__":
    main()
