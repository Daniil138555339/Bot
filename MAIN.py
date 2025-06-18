import telebot
import threading
import time
from random import choice
import requests

TOKEN = '7288423950:AAG2s5EqnsmV3EmzJbhsmaiTzuWfH8Skhlk'  # вставьте сюда ваш токен
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Длина таймера в секундах (например, 10 секунд)
    timer_duration = 10

    # Отправляем сообщение о запуске таймера
    bot.send_message(message.chat.id, f"Таймер запущен на {timer_duration} секунд!")

    # Запускаем отдельный поток для отсчёта времени
    threading.Thread(target=run_timer, args=(message.chat.id, timer_duration)).start()

def run_timer(chat_id, duration):
    time.sleep(duration)
    bot.send_message(chat_id, "Время вышло!")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

# Запуск бота
bot.infinity_polling()