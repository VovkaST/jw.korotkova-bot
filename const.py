from enum import Enum


class Messages(str, Enum):
    START = "Приветственное сообщение"
    HELP = "Текст помощи"
    ABOUT = "Текст обо мне"
    UNKNOWN = "Не разберу... Повтори!"


class Buttons(str, Enum):
    HELP = "Помощь"
    ABOUT = "Обо мне"
