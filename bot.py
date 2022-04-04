from decouple import config
import telebot

TOKEN = config('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'hello':
        bot.send_message(message.from_user.id,
                         f"Hello, how can i help you?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Write 'hello'")
    else:
        bot.send_message(message.from_user.id,
                         "I don't understand you .Write Hello")


bot.polling(none_stop=True, interval=0)
