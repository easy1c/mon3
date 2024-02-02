import asyncio
from aiogram import types
import logging
from bot import bot,dp
from handlers import (
    echo_router,
    start_router,
    images_router,
    shop_router,
    fsm_router,
    router
)
from db import queries
async def on_srartup():
    print('Бот запущен')
    queries.init_db()
    queries.create_tables()
    queries.populate_db()



# обработка команды
async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="pic", description="Отправить картинку"),
        types.BotCommand(command="my_info", description="Моя информация"),
        types.BotCommand(command="startq", description="Начать вопросы")
    ])
    dp.include_router(start_router)
    dp.include_router(images_router)
    dp.include_router(shop_router)
    dp.include_router(fsm_router)
    dp.include_router(router)

    dp.include_router(echo_router)
    dp.startup.register(on_srartup)


    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
