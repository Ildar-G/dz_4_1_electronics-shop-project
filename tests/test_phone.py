import pytest

from src.item import Item
from src.phone import Phone


def test_item_and_phone_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25


def test_phone_and_phone_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 80_000, 2, 3)
    assert phone1 + phone2 == 7


def test_phone_str_method():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_add_method_with_invalid_type():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    with pytest.raises(TypeError) as excinfo:
        result = phone1 + "test"
    assert "Можно сложить только Phone и Item." in str(excinfo.value)


def test_inccorect_number_of_sim():
    with pytest.raises(ValueError) as excinfo:
        phone1 = Phone("iPhone 14", 120000, 5, 0)
    assert "Количество SIM-карт должно быть целым числом больше нуля." in str(excinfo.value)
