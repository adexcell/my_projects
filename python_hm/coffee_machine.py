import json
import random


class CoffeeMachine:
    @staticmethod
    def open_json() -> dict:
        with open('etc.json') as f:
            data = json.load(f)
        return data

    @staticmethod
    def save_changes(data_dict) -> None:
        with open('etc.json', 'w') as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=4)

    data_dict: dict = open_json()
    slogans: list = data_dict.get('slogans', 0)
    cash_box: dict = data_dict.get('cash_box', 0)
    menu: dict = data_dict.get('menu', 0)
    trash_bin: int = data_dict.get('trash_bin', 0)
    water_volume: int = data_dict.get('water', 0)
    banknotes = []
    for i in cash_box.keys():
        banknotes.append(int(i))


class UserInterface(CoffeeMachine):

    def choose_coffee(self):
        self.print_greetings()
        print('Выберите кофе: ')
        menu = self.menu
        menu_keys = []
        for key in menu:
            if menu[key]['quantity'] > 0:  # если кофе не закончилось, добавь его в меню
                menu_keys.append(key)
        for i in range(len(menu_keys)):
            print(f"{i + 1}. {menu_keys[i]} - {menu[menu_keys[i]]['price']} руб, {menu[menu_keys[i]]['volume']}мл, \n"
                  f"{menu[menu_keys[i]]['description']}.")
        number: int = int(input('Введите номер напитка: \n'))
        name: str = menu_keys[number - 1]
        return name

    def print_greetings(self) -> None:
        slogans = self.slogans
        random_number: int = random.randint(0, len(slogans)-1)
        greeting_slogan: str = slogans[random_number]
        greetings = f'Добро пожаловать! {greeting_slogan}'
        print(greetings)

    def get_money(self, name) -> tuple:
        price: int = int(self.menu.get(name).get('price'))
        deposit = 0
        while deposit <= price:
            money = int(input('Внесите купюру, минимум 50 руб. Для прекращения операции введите 0 \n'))
            if money == '0':
                break
            elif money not in self.banknotes:
                print('Введено не корректное значение, повторите')
            else:
                deposit += money
                return deposit, price

    @staticmethod
    def give_change(money):
        print(f'Ваша сдача: {money}')

    @staticmethod
    def return_money(money):
        print(f'Извините! Аппарат не может выдать сдачу! Ваши деньги: {money}')

    @staticmethod
    def pour_coffee(coffee_name):
        machine.make_coffee(coffee_name)
        print(f'Пожалуйста, ваш {coffee_name}!')


class Machine(CoffeeMachine):

    # проверяет есть ли вода в кофеварке, и остались ли места в контейнере пустых капсул
    def checkup_machine(self) -> None:
        if self.water_volume <= 0:
            answer = input("Добавьте воды \n")
            if answer:
                self.data_dict["water"] = 5000
        elif self.trash_bin == 0:
            answer = input("Очистить корзину \n")
            if answer:
                self.data_dict["trash_bin"] = 20
        self.save_changes(self.data_dict)

    def make_coffee(self, name) -> str:
        coffee_value: int = self.menu.get(name).get("volume")
        self.menu[name]["quantity"] -= 1
        self.data_dict["water"] -= coffee_value
        self.data_dict["trash_bin"] -= 1
        self.save_changes(self.data_dict)
        return name

    def calculate_change(self, deposit, price) -> list:
        diff: int = deposit - price
        change = []
        while diff > 0:
            for i in self.banknotes:
                if int(i) <= diff and self.cash_box[str(i)] > 0:
                    change.append(i)
                    self.cash_box[str(i)] -= 1
                    diff -= int(i)
                    self.save_changes(self.data_dict)
        return change


main = UserInterface()
machine = Machine()


def run_coffe_machine():
    machine.checkup_machine()
    coffee_name = main.choose_coffee()
    deposit, coffee_price = main.get_money(coffee_name)
    change = machine.calculate_change(deposit, coffee_price)
    if sum(change) > 0:
        main.give_change(change)
        main.pour_coffee(coffee_name)
    elif sum(change) < 0:
        main.return_money(deposit)


if __name__ == "__main__":
    run_coffe_machine()
