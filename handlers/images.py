from aiogram import types, Router
from aiogram.filters import Command
from random import choice
images_router = Router()
from bot import bot
@images_router.message(Command("pic"))
async def pic(message: types.Message):
    photos = ['qwe.jpeg', 'Unknown.jpeg', 'Unknown-1.jpeg']
    file = types.FSInputFile(f"images/{choice(photos)}")
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=file,
                         caption = 'Hello')