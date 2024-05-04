from pathlib import Path
from config import bot
import knopki
import dannie
import os


def handlers_fun(function_call, user_id):
    request_data = function_call.data
    data_to_message = {
        "inter_zadachi": lambda: send_message(user_id, dannie.wopros_1),
        "dop_uroki": lambda: send_message(user_id, dannie.dop_uroki),
        "spisok_uchenikov": lambda: send_message(user_id, dannie.ucheniki),
        "panidelnik": lambda: send_message(user_id, dannie.panidelnik),
        "vtornik": lambda: send_message(user_id, dannie.vtornik),
        "sreda": lambda: send_message(user_id, dannie.sreda),
        "chetverg": lambda: send_message(user_id, dannie.chetverg),
        "pjatniza": lambda: send_message(user_id, dannie.pjatniza),
        "prepodovateli": lambda: send_message(user_id, dannie.prepodovateli),
        "russki_jazik": lambda: send_images(user_id, folder='russish'),
        "geometrija": lambda: send_images(user_id, folder="geometrish"),
        "algebra": lambda: send_images(user_id, folder="albebra"),
        "fizika": lambda: send_images(user_id, folder="fisish"),
        "VS": lambda: send_images(user_id, folder="vsish"),
        "kalendar": lambda: send_images(user_id, folder="fk/kalendar"),
        "raspisanie": lambda: show_menu(user_id, dannie.vib_den, knopki.dni_ned),
        "back": lambda: show_menu(user_id, dannie.glavnoe_menu, knopki.markup_katalog),
        "formuli": lambda: show_menu(user_id, dannie.vib_pred, knopki.markup_pred),
    }

    message_function = data_to_message.get(request_data)
    if message_function:
        message_function()


def show_menu(user_id, text, markup):
    bot.send_message(user_id, text, reply_markup=markup)


def send_message(user_id, message):
    bot.send_message(user_id, message, reply_markup=knopki.markup_back)


BASE_DIR = Path(__file__).resolve().parent.parent


def send_images(user_id, folder):
    address = f'{BASE_DIR}/source/{folder}'
    for fil_name in os.listdir(address):
        bot.send_photo(user_id, open(os.path.join(address, fil_name), 'rb'))

    bot.send_message(user_id, dannie.vse, reply_markup=knopki.markup_back)
