from aiogram import Bot, Dispatcher, types
from data import config

bot = Bot(config.BOT_TOKEN, parse_mode='HTML')

dp = Dispatcher(bot)