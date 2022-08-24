from aiogram import Bot, Dispatcher, executor, types
TOKEN_API = '5713160005:AAGeGWG666WhRLzqVtm_K4OawCXStPrrxzs'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


if __name__ == '__main__':
    executor.start_polling(dp)