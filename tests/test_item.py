from src.item import Item

"""Тест с использованием pytest для модуля item."""


def test_calculate_total_price():
    item = Item('Test_item', 10.0, 10)
    assert item.calculate_total_price() == 100.0


def test_apply_discount():
    item = Item('Test_item', 100.0, 5)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 80.0
