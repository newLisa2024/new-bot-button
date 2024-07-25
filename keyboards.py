from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def get_main_menu():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Привет"))
    builder.add(KeyboardButton(text="Пока"))
    return builder.as_markup(resize_keyboard=True)

def get_links_menu():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Новости", url="https://news.example.com"))
    builder.add(InlineKeyboardButton(text="Музыка", url="https://music.example.com"))
    builder.add(InlineKeyboardButton(text="Видео", url="https://video.example.com"))
    return builder.as_markup()

def get_dynamic_menu():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))
    return builder.as_markup()

def get_options_menu():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Опция 1", callback_data="option_1"))
    builder.add(InlineKeyboardButton(text="Опция 2", callback_data="option_2"))
    return builder.as_markup()









