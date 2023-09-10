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


class UserInterface(CoffeeMachine):

    def print_greetings(self) -> None:
        slogans = self.slogans
        random_number: int = random.randint(0, len(slogans)-1)
        greeting_slogan: str = slogans[random_number]
        greetings = f'Добро пожаловать! {greeting_slogan}'
        print(greetings)

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

    def get_money(self) -> list:
        values = self.cash_box.keys()
        name = self.choose_coffee()
        price: int = self.menu.get(name).get('price')
        money_in = []
        while True:
            money = input('Внесите купюру, минимум 50 руб. Для прекращения операции введите 0 \n')
            if money == '0':
                break
            elif money not in values:
                print('Введено не корректное значение, повторите')
            else:
                money_in.append(money)
                if sum(money_in) >= price:
                    return money_in

    def give_change(self):
        pass

    @staticmethod
    def pour_coffee():
        print('Пожалуйста, ваш ароматный кофе!')


class Machine(CoffeeMachine):

    def make_coffee(self, name) -> str:
        coffee_value: int = self.menu.get(name).get("volume")
        self.menu[name]["quantity"] -= 1
        self.data_dict["water"] -= coffee_value
        self.data_dict["trash_bin"] -= 1
        self.save_changes(self.data_dict)
        return name

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

    def save_money(self):
        pass

    def calculate_change(self):
        pass



main = UserInterface()
machine = Machine()


def run_coffe_machine():
    machine.checkup_machine()
    main.choose_coffee()


if __name__ == "__main__":
    run_coffe_machine()
