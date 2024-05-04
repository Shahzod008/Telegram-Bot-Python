from telebot.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup)

button_info_1 = {
    "Расписание": 'raspisanie',
    "Все каталоги": 'back',
}

button_info_2 = {
    "Расписание": 'raspisanie',
    "Доп. уроки": 'dop_uroki',
    "Теория уроков": 'formuli',
    "Преподаватели": 'prepodovateli',
    "Список учеников": 'spisok_uchenikov',
    "Интересные задачи": 'inter_zadachi',
    "Календарь учебного года": 'kalendar'
}

button_info_3 = {
    "Понедельник": "panidelnik",
    "Вторник": "vtornik",
    "Среда": "sreda",
    "Четверг": "chetverg",
    "Пятница": "pjatniza",
    "Назад": "back"
}

button_info_4 = {
    "Алгебра": "algebra",
    "Геометрия": "geometrija",
    "Русский язык": "russki_jazik",
    "Физика": "fizika",
    "Вероятность и статистика": "VS",
    "Назад": "back"
}


def mark(_object, _dict):
    for name, callback_data in _dict.items():
        _object.add(InlineKeyboardButton(name, callback_data=callback_data))


markup_start = InlineKeyboardMarkup()
markup_katalog = InlineKeyboardMarkup()
dni_ned = InlineKeyboardMarkup()
markup_pred = InlineKeyboardMarkup()


mark(markup_start, button_info_1)
mark(markup_katalog, button_info_2)
mark(dni_ned, button_info_3)
mark(markup_pred, button_info_4)

markup_back = InlineKeyboardMarkup([[InlineKeyboardButton(text="Назад", callback_data='back')]])
