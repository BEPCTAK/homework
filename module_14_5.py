import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN
from crud_functions import initiate_db, get_all_products, add_user, is_included

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()
    buying = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


# Создание основной клавиатуры
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
button3 = KeyboardButton('Купить')
button4 = KeyboardButton('Регистрация')  # Новая кнопка для регистрации
kb.add(button1, button2, button3, button4)


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
    products = get_all_products()
    for product in products:
        product_id, title, description, price = product
        product_text = f'Название: {title} | Описание: {description} | Цена: {price}'
        await message.answer(product_text)

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)


@dp.message_handler(lambda message: message.text == 'Регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text

    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
        return

    await state.update_data(username=username)
    await message.answer("Введите свой email:")
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = int(message.text)

    user_data = await state.get_data()
    username = user_data.get("username")
    email = user_data.get("email")

    add_user(username, email, age)
    await message.answer("Вы успешно зарегистрированы!")

    await state.finish()


@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    initiate_db()

    executor.start_polling(dp, skip_updates=True)