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

def test_instantiate_from_csv(items):
    assert len(items) == 5  # В файле 5 записей, должно быть 5 объектов
    assert isinstance(items[0], Item)  # Проверяем, что элементы - объекты класса Item


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5