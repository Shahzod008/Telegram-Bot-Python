# Телеграмм бот 

## Отписание

##### **Телеграмм бот** - телеграм бот для Вашего класса, который предоставляет пользователям информацию о расписании занятий, шпаргалки и т.д.

# Технологии

- [Python 3.12](https://www.python.org/downloads/release/python-388/)
- [pyTelegramBotAPI 4.17.0](https://pypi.org/project/pyTelegramBotAPI/)

# Локальная установка

Клонируйте репозиторий и перейдите в него в командной строке:

```sh
git https://github.com/Shahzod008/Telegram-Bot-Python.git
```
Установите зависимостей
```
pip install -r requirements.txt
```
Выполните команду
```sh
cd file_cod_bot
```
В файле config.py добавьте токен вашего бота вместо *Token
```
bot = telebot.TeleBot(token="*Token", parse_mode='html')
```
Выполните команду
```sh
python main.py
```


## Автор:
* [Shahzod008](https://github.com/Shahzod008)