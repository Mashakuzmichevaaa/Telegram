python
import requests
from bs4 import BeautifulSoup
import telebot
import os

# Создание бота и указание токена
bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])

# Функция для получения погоды с сайта gismeteo.ru
def get_weather(city):
    url = f'https://www.gismeteo.ru/weather-{city.lower()}-4248/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    temperature = soup.find('span', class_='js_value tab-weather__value_l').text
    condition = soup.find('div', class_='tab-weather__desc').text
    return f'Температура в {city.capitalize()}: {temperature}\nСостояние: {condition}'

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я могу показать тебе погоду. Просто отправь мне название города.')

# Обработчик сообщений с названием города
@bot.message_handler(content_types=['text'])
def send_weather(message):
    city = message.text
    try:
        weather = get_weather(city)
        bot.send_message(message.chat.id, weather)
    except:
        bot.send_message(message.chat.id, 'К сожалению, я не могу получить погоду для этого города.')

# Запуск бота
bot.polling()
