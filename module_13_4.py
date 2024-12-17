from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

API = ''



bot = Bot(token=API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Напишите 'Calories', чтобы начать ввод данных.")

@dp.message_handler(lambda message: message.text == 'Calories')
async def set_age(message: types.Message):
    await UserState.age.set()
    await message.answer("Введите свой возраст:")

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
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)

    data = await state.get_data()


    age = int(data.get('age', 0))
    growth = int(data.get('growth', 0))
    weight = int(data.get('weight', 0))

    # Формула Миффлина - Сан Жеора (для женщин)
    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")

    await state.finish()

@dp.message_handler()
async def all_messages(message:types.Message):
    await message.answer("Напишите '/start', чтобы начать общение.")


if __name__ == '__main__':
    print("Запуск бота...")
    executor.start_polling(dp, skip_updates=True)
