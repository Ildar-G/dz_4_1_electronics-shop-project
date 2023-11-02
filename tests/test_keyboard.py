import pytest

from src.keyboard import Keyboard


def test_keyboard_creation():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert kb.price == 9600
    assert kb.quantity == 5


def test_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


def test_object_has_no_setter():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError) as excinfo:
        kb.language = 'CH'
    assert "property 'language' of 'Keyboard' object has no setter" in str(excinfo.value)
