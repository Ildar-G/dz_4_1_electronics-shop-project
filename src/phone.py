from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        """
        Реализация операции сложения для экземпляров классов Phone и Item.
        Сложение происходит по количеству товара в магазине.
        """
        if not isinstance(other, (Phone, Item)):
            raise TypeError("Можно сложить только Phone и Item.")

        return self.quantity + other.quantity

    @property
    def number_of_sim(self) -> int:
        """
                Получение количества поддерживаемых сим-карт.
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        """
        Установка количества поддерживаемых сим-карт.
        """
        if value < 1:
            raise ValueError("Количество SIM-карт должно быть целым неотрицательным числом.")
        self._number_of_sim = value

    def __repr__(self):
        """
        Метод repr для представления объекта в виде строки.
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
