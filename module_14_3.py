import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()
    buying = State()

# Создание основной клавиатуры
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
button3 = KeyboardButton('Купить')
kb.add(button1, button2, button3)

# Создание Inline-клавиатуры
inline_keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton('Product1', callback_data='product_buying')
button2 = InlineKeyboardButton('Product2', callback_data='product_buying')
button3 = InlineKeyboardButton('Product3', callback_data='product_buying')
button4 = InlineKeyboardButton('Product4', callback_data='product_buying')
inline_keyboard.add(button1, button2, button3, button4)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=kb)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

@dp.message_handler(lambda message: message.text == 'Информация')
async def send_info(message: types.Message):
    info_text = (
        "Этот бот поможет вам рассчитать вашу норму калорий.\n"
        "Введите свой возраст, рост и вес, и я вычислю вашу норму калорий."
    )
    await message.answer(info_text)

@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        product_text = f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}'
        await message.answer(product_text)
        photo_path = f'product{i}.jpg'
        await message.answer_photo(photo=types.InputFile(photo_path))
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)