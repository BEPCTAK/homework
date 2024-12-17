from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor



api = ""

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Приветствую тебя!Спроси меня: как дела?")


@dp.message_handler(text = ["как дела?"])
async def time_message(message):
    await message.answer("Спасибо, лучше всех, никто не завидует! ")


@dp.message_handler()
async def all_messages(message:types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)