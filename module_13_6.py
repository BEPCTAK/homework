import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = ''

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()

# Создание основной клавиатуры
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
kb.add(button1, button2)

# Создание Inline-клавиатуры
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=kb)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formulas_text = (
        "Формула Миффлина - Сан Жеора (для женщин):\n"
        "Калории = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161\n"
        "Формула Миффлина - Сан Жеора (для мужчин):\n"
        "Калории = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    )
    await call.message.answer(formulas_text)
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer("Введите свой рост:")

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer("Введите свой вес:")

@dp.message_handler(state=UserState.weight)
async def set_gender(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await UserState.gender.set()
    await message.answer("Введите свой пол (муж/жен):")

@dp.message_handler(state=UserState.gender)
async def send_calories(message: types.Message, state: FSMContext):
        await state.update_data(gender=message.text)

        data = await state.get_data()

        age = int(data.get('age', 0))
        growth = int(data.get('growth', 0))
        weight = int(data.get('weight', 0))
        gender = data.get('gender', 'male')

    # Формула Миффлина - Сан Жеора (для женщин)
        calories1 = 10 * weight + 6.25 * growth - 5 * age - 161
        calories2 = 10 * weight + 6.25 * growth - 5 * age + 5

        if gender == 'муж':
          calories = calories2
        else:
          calories = calories1

        await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
        await state.finish()

@dp.message_handler(lambda message: message.text == 'Информация')
async def send_info(message: types.Message):
    info_text = (
        "Этот бот поможет вам рассчитать вашу норму калорий.\n"
        "Введите свой возраст, рост и вес, и я вычислю вашу норму калорий."
    )
    await message.answer(info_text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)