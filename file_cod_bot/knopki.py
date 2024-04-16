from telebot import types

button_info_1 = {
    "Расписание": 'raspisanie',
    "Все каталоги": 'back',
}

markup_start = types.InlineKeyboardMarkup()
for name, callback_data in button_info_1.items():
    markup_start.add(types.InlineKeyboardButton(name, callback_data=callback_data))
markup_start.add(types.InlineKeyboardButton("Если бот перестал работать напишите сюда", url="https://t.me/Shahzod_01_01_01"))


button_info_2 = {
    "Расписание": 'raspisanie',
    "Доп. уроки": 'dop_uroki',
    "Теория уроков": 'formuli',
    "Преподаватели": 'prepodovateli',
    "Список учеников": 'spisok_uchenikov',
    "Интересные задачи": 'inter_zadachi',
    "Календарь учебного года": 'kalendar'
}

markup_katalog = types.InlineKeyboardMarkup()
for name, callback_data in button_info_2.items():
    markup_katalog.add(types.InlineKeyboardButton(name, callback_data=callback_data))
markup_katalog.add(types.InlineKeyboardButton("Если бот перестал работать напишите сюда", url="https://t.me/Shahzod_01_01_01"))


button_info_3 = {
    "Понедельник": "panidelnik",
    "Вторник": "vtornik",
    "Среда": "sreda",
    "Четверг": "chetverg",
    "Пятница": "pjatniza",
    "Назад": "back"
}

dni_ned = types.InlineKeyboardMarkup()
for name, callback_data in button_info_3.items():
    dni_ned.add(types.InlineKeyboardButton(name, callback_data=callback_data))


button_info_4 = {
    "Алгебра": "algebra",
    "Геометрия": "geometrija",
    "Русский язык": "russki_jazik",
    "Физика": "fizika",
    "Вероятность и статистика": "VS",
    "Назад": "back"
}

markup_pred = types.InlineKeyboardMarkup()
for name, callback_data in button_info_4.items():
    markup_pred.add(types.InlineKeyboardButton(name, callback_data=callback_data))


markup_back = types.InlineKeyboardMarkup(
    keyboard=[
        [types.InlineKeyboardButton(
            text="Назад",
            callback_data='back'
        )]
    ]
)
