cash_register = {5000: 2,
                 2000: 0,
                 1000: 5,
                 500: 5,
                 200: 0,
                 100: 0,
                 50: 3}
banknotes = list(cash_register.keys())
cash_in = []


def get_cash(price):
    cash = 0
    while True:
        try:
            cash_in = list(map(int, input('Введите номиналы через пробел, минимум 50 рублей: ').split(' ')))
            # Здесь нужна проверка вносит ли пользователь купюры от 50 рублей, с написанием предупреждения если нет
            for n in cash_in:
                if n not in banknotes:
                    raise ValueError
                else:
                    cash_register[n] += 1
                    cash += n
        except ValueError:
            print('Нужно ввести номиналы реальных банкнот через пробел! \n')
        else:
            if cash >= price:
                return cash
            else:
                print('Суммы недостаточно!')
                answer = input('Хотите внести ещё? - Да/Нет ')
                if answer == 'Нет':
                    return print(f'Возврат денег: {cash}')
                elif answer == 'Да':
                    continue
                else:
                    print(f'Введена недопустимая команда! Возврат денег: {cash}')
                    break


def calculate_change(price, name):
    try:
        cash = get_cash(price)
        diff = cash - price
        while diff > 0 and cash_register[50] > 0:
            for i in banknotes:
                if i <= diff and cash_register[i] > 0:
                    cash_in.append(i)
                    cash_register[i] -= 1
                    diff -= i
        if diff == 0:
            print(f'Ваш {name}! Ваша сдача {cash_in}')
            cash_in.clear()
        else:
            for n in cash_in:
                cash_register[n] += 1
            cash_register[cash] -= 1
        cash_in.clear()
        return f'Недостаточно средств в кассе для выдачи сдачи! Возврат суммы: {cash}'
    except TypeError:
        pass
print(cash_in)

if __name__ == '__main__':
    print(calculate_change(150, 'эспрессо'))
    print(cash_in)
