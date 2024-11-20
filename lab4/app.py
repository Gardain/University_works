import logging
import requests
import folium
import os
import json
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

# Настройки
API_TOKEN = "ВАШ_ТОКЕН"
NASA_API_KEY = "ВАШ_КЛЮЧ"
USER_DATA_FILE = "user_data.json"  # Файл для хранения пользовательских данных

# Логирование
logging.basicConfig(level=logging.INFO)


# Функции для загрузки/сохранения пользовательских данных
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}


def save_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Загрузка данных при запуске
user_data = load_user_data()


# Состояния для FSM
class SaveNumberStates(StatesGroup):
    waiting_for_number = State()


# Обработчик команды /start
async def start_command(message: Message):
    await message.answer(
        "Привет! Я космический бот 🚀. Вот что я умею:\n"
        "/iss_location - Текущее местоположение МКС\n"
        "/people_in_space - Кто сейчас в космосе?\n"
        "/nasa_apod - Картинка дня от NASA\n"
        "/random_fact - Интересный факт о космосе\n"
        "/save_number - Сохранить число\n"
        "/get_number - Посмотреть сохраненное число"
    )


# Сохранение числа (начало)
async def save_number_command(message: Message, state: FSMContext):
    await message.answer("Введите число, которое хотите сохранить:")
    await state.set_state(SaveNumberStates.waiting_for_number)


# Сохранение числа (ввод числа)
async def handle_number(message: Message, state: FSMContext):
    try:
        number = int(message.text)
        user_id = str(message.from_user.id)
        user_data[user_id] = number
        save_user_data(user_data)
        await message.answer(f"Ваше число {number} сохранено!")
        await state.clear()  # Завершаем состояние
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число.")


# Получение сохраненного числа
async def get_number_command(message: Message):
    user_id = str(message.from_user.id)
    if user_id in user_data:
        await message.answer(f"Ваше сохраненное число: {user_data[user_id]}")
    else:
        await message.answer("Вы еще не сохраняли число. Используйте /save_number для сохранения.")


# Текущее местоположение МКС
async def iss_location(message: Message):
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]["longitude"])

        # Визуализация позиции на карте
        iss_map = folium.Map(location=[latitude, longitude], zoom_start=4)
        folium.Marker([latitude, longitude], popup="МКС здесь!").add_to(iss_map)
        map_file = "iss_location.html"
        iss_map.save(map_file)

        # Отправка карты пользователю
        await message.answer_document(FSInputFile(map_file))
        os.remove(map_file)
    else:
        await message.answer("Не удалось получить данные о МКС. Попробуйте позже.")


# Кто сейчас в космосе
async def people_in_space(message: Message):
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        people = "\n".join(
            f"- {person['name']} ({person['craft']})" for person in data["people"]
        )
        await message.answer(f"Сейчас в космосе {data['number']} человек(а):\n{people}")
    else:
        await message.answer("Не удалось получить данные о людях в космосе.")


# Картинка дня от NASA
async def nasa_apod(message: Message):
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        title = data["title"]
        explanation = data["explanation"]
        image_url = data["url"]
        await message.answer_photo(photo=image_url, caption=f"{title}\n\n{explanation}")
    else:
        await message.answer("Не удалось получить картинку дня от NASA. Попробуйте позже.")


# Интересный факт о космосе
async def random_fact(message: Message):
    facts = [
        "Венера — единственная планета, которая вращается в обратном направлении.",
        "Космическая пыль ежегодно попадает на Землю в количестве 40 000 тонн.",
        "Солнце составляет более 99% массы нашей Солнечной системы.",
        "На Луне нет атмосферы, поэтому там нет звуков."
    ]
    from random import choice
    await message.answer(f"Интересный факт: {choice(facts)}")


# Основная функция
async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Регистрируем обработчики
    dp.message.register(start_command, Command("start"))
    dp.message.register(save_number_command, Command("save_number"))
    dp.message.register(handle_number, SaveNumberStates.waiting_for_number)  # FSM обработчик
    dp.message.register(get_number_command, Command("get_number"))
    dp.message.register(iss_location, Command("iss_location"))
    dp.message.register(people_in_space, Command("people_in_space"))
    dp.message.register(nasa_apod, Command("nasa_apod"))
    dp.message.register(random_fact, Command("random_fact"))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


# Запуск
if __name__ == "__main__":
    asyncio.run(main())
