import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
import keyboards as kb
from aiogram.fsm.storage.memory import MemoryStorage

async def main():
    # Создание бота и диспетчера
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Обработчик команды /start
    @dp.message(CommandStart())
    async def send_welcome(message: Message):
        await message.answer("Меню:", reply_markup=kb.get_main_menu())

    # Обработчик команды /links
    @dp.message(Command(commands=['links']))
    async def send_links(message: Message):
        await message.answer("Выберите ссылку:", reply_markup=kb.get_links_menu())

    # Обработчик команды /dynamic
    @dp.message(Command(commands=['dynamic']))
    async def send_dynamic(message: Message):
        await message.answer("Динамическое меню:", reply_markup=kb.get_dynamic_menu())

    # Обработчик нажатий на инлайн-кнопки
    @dp.callback_query(lambda callback_query: callback_query.data == "show_more")
    async def process_show_more(callback_query: CallbackQuery):
        await callback_query.message.edit_reply_markup(reply_markup=kb.get_options_menu())
        await callback_query.answer()

    @dp.callback_query(lambda callback_query: callback_query.data == "option_1")
    async def process_option_1(callback_query: CallbackQuery):
        await callback_query.message.answer("Какая хорошая погода!")
        await callback_query.answer()

    @dp.callback_query(lambda callback_query: callback_query.data == "option_2")
    async def process_option_2(callback_query: CallbackQuery):
        await callback_query.message.answer("Отличное настроение!")
        await callback_query.answer()

    @dp.callback_query(lambda callback_query: callback_query.data == "hello")
    async def process_hello(callback_query: CallbackQuery):
        await callback_query.message.answer(f"Привет, {callback_query.from_user.first_name}!")
        await callback_query.answer()

    @dp.callback_query(lambda callback_query: callback_query.data == "bye")
    async def process_bye(callback_query: CallbackQuery):
        await callback_query.message.answer(f"До свидания, {callback_query.from_user.first}!")
        await callback_query.answer()

        # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())





