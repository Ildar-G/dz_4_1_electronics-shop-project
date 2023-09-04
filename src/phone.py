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