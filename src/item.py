import csv
import os


class InstantiateCSVError(Exception):
    FILE_CORRUPTED = "Файл item.csv поврежден или пуст"
    INVALID_DATA = "Некорректные данные в файле item.csv"


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
        try:
            with open(file_path, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError(InstantiateCSVError.FILE_CORRUPTED)
                for row in reader:
                    try:
                        price = cls.string_to_number(row['price'])
                        quantity = cls.string_to_number(row['quantity'])
                    except ValueError:
                        raise InstantiateCSVError(InstantiateCSVError.INVALID_DATA)
                    name = row['name']
                    item = cls(name, price, quantity)
                    items.append(item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        else:
            return items

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
