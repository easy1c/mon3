from aiogram import Router, types
from aiogram.filters import  Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

kw_router = Router()
class KW(StatesGroup):
    name = State()
    age = State()
    napravlenie =State()
    phone = State()
