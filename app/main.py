import asyncio
from aiogram import  Bot , Dispatcher

from app.handlers import router

async def main():
    bot = Bot(token='7711511447:AAF4LTtEbHteKL4jdSyGrvV7HdiFBLtctwI')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('бот-121 выключен')