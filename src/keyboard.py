from src.item import Item


class LanguageMixin:
    def __init__(self, language="EN"):
        self.__language = language


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self, language)