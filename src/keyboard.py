from src.item import Item


class LanguageMixin:
    """Класс миксин для изменения раскладки клавиатуры"""

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Метод для изменения раскладки клавиатуры"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self, language)
