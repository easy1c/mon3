from aiogram import Router, types, F
from aiogram.filters import  Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


fsm_router = Router()
class KW(StatesGroup):
    name = State()
    age = State()
    education =State()
    singer = State()

@fsm_router.message(Command('stop'))
@fsm_router.message(F.text.lower() == "stop")
async def stop(message: types.Message, state:FSMContext):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Опрос окончен!!! ', reply_markup=kb)
    await state.clear()

@fsm_router.message(Command('startq'))
async def kw_router(message:types.Message, state:FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard = [
            [types.KeyboardButton (text = 'Stop'),]
        ]
    )
    await message.answer('Напишите ваше имя ', reply_markup = kb)
    await state.set_state(KW.name)
@fsm_router.message(KW.name)
async def name(message:types.Message, state:FSMContext):
    await message.answer('Напишите ваш возраст ')
    await state.set_state(KW.age)
@fsm_router.message(KW.age)
async def age(message:types.Message, state:FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer('Напишите только цифры')
    else:
        if 10>int(age) or int (age) > 80:
            await message.answer('Лимит по возрасту ')
        else:
            await message.answer('Какое у вас образование')
            await state.set_state(KW.education)
@fsm_router.message(KW.education)
async def education (message:types.Message, state:FSMContext):
    await message.answer('Ваш любимый певец ')
    await state.set_state(KW.singer)

@fsm_router.message(KW.singer)
async def singer (message:types.Message, state:FSMContext):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Опрос окончен!!! ', reply_markup= kb)
    await state.clear()

