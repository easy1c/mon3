from aiogram import types, Router, F
from aiogram.filters import Command
from pprint import pprint
from db.queries import get_courses
router = Router()

@router.callback_query(F.data == 'books')
async def Info(callback:types.CallbackQuery):
    books = get_courses()
    for i in books:
         await callback.message.answer (i[1])
