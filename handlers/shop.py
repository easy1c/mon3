from aiogram import types, Router, F
shop_router = Router()

@shop_router.callback_query(F.data == 'Shop')
async def Shop(callback:types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard = [
            [types.KeyboardButton (text = 'Books'),
             types.KeyboardButton (text = 'Manga'),
             types.KeyboardButton (text = 'Comiks')]
        ]
    )

    await callback.message.answer ('Shop', reply_markup = kb)
@shop_router.message(F.text == 'Books')
async def Books(message:types.Message):
    await message.answer ('Учение свет')

@shop_router.message(F.text == 'Manga')
async def Manga(message: types.Message):
    await message.answer('Japan')
@shop_router.message(F.text == 'Comiks')
async def Comiks(message:types.Message):
    await message.answer ('Marvel')



