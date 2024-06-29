from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

paid = InlineKeyboardButton("Я оплатил ✅", callback_data = "paid")
askQuestion = InlineKeyboardButton("Я хочу задать вопрос❓", callback_data = "askQuestion")
