import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from pprint import pprint
from random import choice


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()


# обработка команды

@dp.message(Command("start"))
async def start(message: types.Message):
    pprint(message)
    await message.answer(f"Привет! {message.from_user.full_name}, ваш id: {message.from_user.id}")


@dp.message(Command("pic"))
async def pic(message: types.Message):
    photos = ['qwe.jpeg', 'Unknown.jpeg', 'Unknown-1.jpeg']
    file = types.FSInputFile(f"images/{choice(photos)}")
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=file,
                         caption = 'Hello')
@dp.message(Command('my_info'))
async def my_info(message: types.Message):
    username = message.from_user.username
    tg_id = message.from_user.id
    firstname= message.from_user.first_name
    lastname= message.from_user.last_name
    await message.answer(f'Ваш username @{username},\n'
                         f'Ваш tg_id {tg_id}\n'
                         f'Ваш firstname {firstname}\n'
                         f'Ваш lastname {lastname}\n')

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="pic", description="Отправить картинку"),
        types.BotCommand(command="my_info", description="Моя информация")
    ])
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
