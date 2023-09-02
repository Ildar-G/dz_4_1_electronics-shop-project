import csv
import os


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
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Получение названия товара.
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Установка названия товара.
        """
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализация экземпляров класса Item данными из файла items.csv.
        :return: Список экземпляров класса Item.
        """
        src_directory = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        file_path = os.path.join(src_directory, 'items.csv')
        items = []
        with open(file_path, encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                price = cls.string_to_number(row["price"])
                quantity = cls.string_to_number(row["quantity"])
                name = row["name"]
                item = cls(name, price, quantity)
                items.append(item)
        return items

    @classmethod
    def remove_item(cls, item):
        """
        Удаление объекта item из списка all.
        """
        cls.all.remove(item)

    def string_to_number(value: str) -> int:
        """
        Преобразование числа-строки в число.
        """
        return int(float(value))

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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'
