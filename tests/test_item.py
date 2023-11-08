import pytest

from src.item import Item, InstantiateCSVError

"""Тест с использованием pytest для модуля item."""


def test_calculate_total_price():
    item = Item('Test_item', 10.0, 10)
    assert item.calculate_total_price() == 100.0


def test_apply_discount():
    item = Item('Test_item', 100.0, 5)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 80.0


@pytest.fixture
def items():
    return Item.instantiate_from_csv()


def test_instantiate_from_csv(items):
    assert len(items) == 5  # В файле 5 записей, должно быть 5 объектов
    assert isinstance(items[0], Item)  # Проверяем, что элементы - объекты класса Item


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'


def test_add_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 120_000, 5)
    assert item1 + item2 == 25


def test_item_name_setter_limit(items):
    item = items[1]
    item.name = 'Короткое'
    assert item.name == 'Короткое'
    item.name = 'Слишком Длинное Название Товара'
    assert item.name == 'Слишком Дл'


def test_item_name_property(items):
    item = items[0]
    assert item.name == 'Смартфон'
    item.name = 'Айфон'
    assert item.name == 'Айфон'


def test_add_method_with_invalid_type():
    item1 = Item("Смартфон", 10000, 20)
    with pytest.raises(TypeError) as excinfo:
        result = item1 + 5
    assert "Можно сложить только Item." in str(excinfo.value)


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_file_corrupted():
    with pytest.raises(InstantiateCSVError, match=InstantiateCSVError.FILE_CORRUPTED):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_file_invalid_data():
    with pytest.raises(InstantiateCSVError, match=InstantiateCSVError.INVALID_DATA):
        Item.instantiate_from_csv()
