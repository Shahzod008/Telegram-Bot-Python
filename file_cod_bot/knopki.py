from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

button_info_1 = {
    "Расписание": 'raspisanie',
    "Все каталоги": 'back',
}

markup_start = InlineKeyboardMarkup()
for name, callback_data in button_info_1.items():
    markup_start.add(
        InlineKeyboardButton(
            name,
            callback_data=callback_data
        )
    )
markup_start.add(
    InlineKeyboardButton(
        text="Если бот перестал работать напишите сюда",
        url="https://t.me/Shahzod_01_01_01"
    )
)


button_info_2 = {
    "Расписание": 'raspisanie',
    "Доп. уроки": 'dop_uroki',
    "Теория уроков": 'formuli',
    "Преподаватели": 'prepodovateli',
    "Список учеников": 'spisok_uchenikov',
    "Интересные задачи": 'inter_zadachi',
    "Календарь учебного года": 'kalendar'
}

markup_katalog = InlineKeyboardMarkup()
for name, callback_data in button_info_2.items():
    markup_katalog.add(
        InlineKeyboardButton(
            name,
            callback_data=callback_data
        )
    )
markup_katalog.add(
    InlineKeyboardButton(
        text="Если бот перестал работать напишите сюда",
        url="https://t.me/Shahzod_01_01_01"
    )
)


button_info_3 = {
    "Понедельник": "panidelnik",
    "Вторник": "vtornik",
    "Среда": "sreda",
    "Четверг": "chetverg",
    "Пятница": "pjatniza",
    "Назад": "back"
}

dni_ned = InlineKeyboardMarkup()
for name, callback_data in button_info_3.items():
    dni_ned.add(
        InlineKeyboardButton(
            name,
            callback_data=callback_data
        )
    )


button_info_4 = {
    "Алгебра": "algebra",
    "Геометрия": "geometrija",
    "Русский язык": "russki_jazik",
    "Физика": "fizika",
    "Вероятность и статистика": "VS",
    "Назад": "back"
}

markup_pred = InlineKeyboardMarkup()
for name, callback_data in button_info_4.items():
    markup_pred.add(
        InlineKeyboardButton(
            name,
            callback_data=callback_data
        )
    )


markup_back = InlineKeyboardMarkup(
    keyboard=[
        [InlineKeyboardButton(
            text="Назад",
            callback_data='back'
        )]
    ]
)
