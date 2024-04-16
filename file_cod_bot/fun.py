import os
from config import bot
from knopki import markup_back, dni_ned, markup_katalog, markup_pred
from dannie import (wopros_1, dop_uroki, ucheniki, panidelnik, vtornik, sreda,
                    chetverg, pjatniza, prepodovateli, vse, vib_den, vib_pred, glavnoe_menu)


def chshoto(function_call, user_id):
    data_to_message = {
        "inter_zadachi": wopros_1,
        "dop_uroki": dop_uroki,
        "spisok_uchenikov": ucheniki,
        "panidelnik": panidelnik,
        "vtornik": vtornik,
        "sreda": sreda,
        "chetverg": chetverg,
        "pjatniza": pjatniza,
        "prepodovateli": prepodovateli
    }
    if function_call.data in data_to_message:
        message = data_to_message[function_call.data]
        bot.send_message(user_id, message, reply_markup=markup_back)

    data_to_range = {
        "russki_jazik": 'russish',
        "geometrija": 'geometrish',
        "algebra": 'albebra',
        "fizika": 'fisish',
        "VS": 'vsish',
        "kalendar": 'fk/kalendar',
    }

    if function_call.data in data_to_range:
        adr = data_to_range[function_call.data]

        adres = f'../source/{adr}'
        for filename in os.listdir(adres):
            bot.send_photo(user_id, open(os.path.join(adres, filename), 'rb'))
        bot.send_message(user_id, vse, reply_markup=markup_back)

    if_elif_else = {
        "raspisanie": (vib_den, dni_ned),
        "back": (glavnoe_menu, markup_katalog),
        "formuli": (vib_pred, markup_pred)
    }

    if function_call.data in if_elif_else:
        text, markup = if_elif_else[function_call.data]
        bot.send_message(user_id, text, reply_markup=markup)
