
from aiogram import types, Router, F
from aiogram.filters import Command
from pprint import pprint

start_router = Router()
@start_router.message(Command("start"))
async def start(message: types.Message):
    pprint(message)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text = 'Info', callback_data= 'Info'),
             types.InlineKeyboardButton(text= 'Shop', callback_data= 'Shop')]
        ]
    )

    await message.answer(f"Привет! {message.from_user.full_name}, ваш id: {message.from_user.id}",
                         reply_markup = kb)

@start_router.callback_query(F.data == 'Info')
async def Info(callback:types.CallbackQuery):
    await callback.message.answer ('Information')

@start_router.message(Command('my_info'))
async def my_info(message: types.Message):
    username = message.from_user.username
    tg_id = message.from_user.id
    firstname= message.from_user.first_name
    lastname= message.from_user.last_name
    await message.answer(f'Ваш username @{username},\n'
                         f'Ваш tg_id {tg_id}\n'
                         f'Ваш firstname {firstname}\n'
                         f'Ваш lastname {lastname}\n')
