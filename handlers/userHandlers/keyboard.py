from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

paid = InlineKeyboardButton("Оплачено", callback_data = "paid")
askQuestion = InlineKeyboardButton("Задать вопрос", callback_data = "askQuestion")
