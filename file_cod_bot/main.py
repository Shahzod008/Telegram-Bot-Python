from config import bot
from knopki import markup_start
from fun import chshoto
import wiki


@bot.message_handler(commands=['start'])
def start(message):
    us_nam = message.from_user.first_name
    us_id = message.chat.id
    bot.send_photo(us_id, open("../source/fk/Приветствие.png", 'rb'))
    bot.send_message(us_id, f"<b>{us_nam}</b>, привет!\nВыбери что тебя интересует", reply_markup=markup_start)


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    user_id = function_call.message.chat.id
    chshoto(function_call, user_id)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, wiki.getwiki(message.text))


bot.polling()
