import asyncio
import os
import logging
import sys
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Filter, CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
load_dotenv()  


token=os.environ.get("token")
dp = Dispatcher()

builder = InlineKeyboardBuilder()
builder.button(text=f"Наш сайт", web_app=types.WebAppInfo(url="https://youtu.be"))

@dp.message(CommandStart())
async def process_start_command(message: types.Message):

    await message.answer("Нажмите на кнопку, чтобы открыть веб-приложение.", reply_markup=builder.as_markup())

async def main() -> None:
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())