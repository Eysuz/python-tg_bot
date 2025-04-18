from telebot import TeleBot, types

TOKEN = "8079103208:AAEkCxhBD3s3Y9iZGdxecbeSY-v5FEwhT30"
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)



    buttons = [
        types.KeyboardButton("📍 Joylashuv yuborish", request_location=True),
        types.KeyboardButton("📞 Kontaktni yuborish", request_contact=True),
        types.KeyboardButton("❌ Bekor qilish")
     ]
    markup.add(*buttons)


    bot.send_message(
        chat_id=message.chat.id,
        text="quyidagi opsiyalardan birini tanlang",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: True)
def handle_options(message):
    """Handle user responses from the menu.""" 
    if message.text == "❌ Bekor qilish":
        bot.send_message(chat_id=message.chat.id, text="Amal bekor qilindi")
    else:  
        bot.send_message(chat_id=message.chat.id, text="Sizning javobingiz qabul  qilindi")


if __name__ == "__main__":
    bot.polling()