from aiogram import types, Router, F
from aiogram.filters import Command
from pprint import pprint
from db.queries import get_courses, get_books_by_type
router = Router()

@router.callback_query(F.data == 'books')
async def Info(callback:types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text = 'книга', callback_data= '1'),
             types.InlineKeyboardButton(text= 'комииксы', callback_data= '2'),
             types.InlineKeyboardButton(text= 'манга', callback_data= '3')]
        ]
    )
    await callback.message.answer('что вас интересует?', reply_markup=kb)

@router.callback_query(F.data == '1')
async def get_books(call:types.CallbackQuery):
    object = get_books_by_type(1)
    for i in object:
        await  call.message.answer(f"{i[1]}\n"
                                   f"{i[2]}som\n"
                                   f"книги")

@router.callback_query(F.data == '2')
async def get_comics(call:types.CallbackQuery):
    object = get_books_by_type(2)
    for i in object:
        await  call.message.answer(f"{i[1]}\n"
                                   f"{i[2]}som\n"
                                   f"комиксы")

@router.callback_query(F.data == '3')
async def get_manga(call:types.CallbackQuery):
    object = get_books_by_type(3)
    for i in object:
        await  call.message.answer(f"{i[1]}\n"
                                   f"{i[2]}som\n"
                                   f"манга")