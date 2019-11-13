import telebot
import pyowm

owm = pyowm.OWM('Weather API')
bot = telebot.TeleBot("Bot API")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, how are you doing?")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()

    answer = "Status: " + w.get_status() + "\n\n"
    answer += "Detailed status: " + w.get_detailed_status() + "\n"
    answer += "Temperature: " + \
        str(w.get_temperature('celsius')['temp']) + "\n"
    answer += "Min temperature: " + \
        str(w.get_temperature('celsius')['temp_min']) + "\n"
    answer += "Max temperature: " + \
        str(w.get_temperature('celsius')['temp_max']) + "\n"
    answer += "Wind speed: " + str(w.get_wind()['speed'])

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
