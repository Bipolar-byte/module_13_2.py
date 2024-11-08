from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import random

api = ""

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

health_tips = [
    "Пейте больше воды каждый день.",
    "Регулярно занимайтесь физическими упражнениями.",
    "Старайтесь спать не менее 7-8 часов каждую ночь.",
    "Питайтесь разнообразно и включайте в рацион свежие фрукты и овощи.",
    "Регулярно делайте перерывы во время работы для отдыха глаз и тела."
]


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    print("Привет! Я бот, помогающий твоему здоровью.")
    await message.reply("Привет! Я бот, помогающий твоему здоровью. Введите /help, чтобы узнать доступные команды.")


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    help_text = (
        "Я помогу тебе заботиться о здоровье!\n"
        "Доступные команды:\n"
        "/start - начать общение с ботом\n"
        "/help - получить список команд\n"
        "/tips - получить случайный совет по здоровью\n"
        "/about - узнать больше обо мне"
    )
    print("Команда /help вызвана.")
    await message.reply(help_text)


@dp.message_handler(commands=["tips"])
async def tips_command(message: types.Message):
    tip = random.choice(health_tips)
    print("Отправлен совет по здоровью:", tip)
    await message.reply(tip)


@dp.message_handler(commands=["about"])
async def about_command(message: types.Message):
    about_text = (
        "Я бот, созданный, чтобы помогать вам заботиться о здоровье. "
        "Я могу давать советы, напоминать о важности отдыха и физической активности. "
        "Надеюсь быть полезным!"
    )
    print("Команда /about вызвана.")
    await message.reply(about_text)


@dp.message_handler()
async def all_massages(message: types.Message):
    print("Введите команду /start, чтобы начать общение.")
    await message.reply("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
