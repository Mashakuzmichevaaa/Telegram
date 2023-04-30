python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from bs4 import BeautifulSoup

TOKEN = '6218817632:AAHzYGdaMaDD3VuFfgA213pB4qxPEDsgVAw'
bot = telebot.TeleBot(TOKEN)
# URL для получения погоды для Москвы на сайте gismeteo.ru
URL = 'https://www.gismeteo.ru/weather-moscow-4368/'

# Функция для получения погоды с сайта gismeteo.ru
def get_weather():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Здесь можно выбрать нужные данные о погоде из HTML страницы
    temperature = soup.find('div', class_='js_value tab-weather__value_l').text
    condition = soup.find('div', class_='tab-weather__desc').text
    return f'Температура: {temperature}\nСостояние: {condition}'

# Обработчик команды /start
def start(update, context):
    update.message.reply_text('Привет! Я могу показать тебе погоду. Просто отправь мне команду /weather.')

# Обработчик команды /weather
def weather(update, context):
    weather = get_weather()
    update.message.reply_text(weather)

# Функция для запуска бота
def main():
    updater = Updater('your_bot_token', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("weather", weather))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()