import csv
import os

CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'items.csv'))


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, ):
        """
        Считываем файл и инициализируем экземпляры класса

        """
        items = []
        with open(CSV_PATH, 'r', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            next(reader)
            for data in reader:
                item = cls(data['name'], float(data['price']), int(data['quantity']))
                # cls.all.append(item)
                items.append(item)
            return items

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Преобразуем число из строки
        """
        return int(number.split(".")[0])

    @property
    def name(self):
        """
        Геттер для названия товара
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Сеттер для названия товара
        """
        if len(value) <= 10:
            self.__name = value
        else:
            print("Длинна наименования товара превышает 10 символов ")

    def __add__(self, other):
        """
        Реализуем метод сложения двух классов по количеству товара
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None
        # if issubclass(other.__class__, self.__class__):
        #     return self.quantity + other.quantity
        # return None
