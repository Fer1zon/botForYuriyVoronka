from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State

from pathlib import Path

import sys 
import os 
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from importantFiles.config import channelLink, channel, sendNotificationId

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup






async def startBotHandlerUser(message : types.Message):
    await message.answer_video_note(video_note="BAACAgIAAxkBAALSb2ZxwP8pJohDxI34sFnInJs3t1LSAALNVAACgCaRSxjR33cmkWZbNQQ")
    with open(Path("utils","messageContent","startMessageContent","textStartMessage.txt"), "r", encoding="utf-8") as textFile:
        sendText = textFile.read()

    with open(Path("utils","messageContent","startMessageContent","imgStartMessage.txt"), "r", encoding="utf-8") as imgFile:
        sendImg = imgFile.read()

    subscribe = InlineKeyboardButton("Подписаться", url = channelLink)
    check = InlineKeyboardButton("Готово", callback_data = "check")

    keyboard = InlineKeyboardMarkup(row_width=1).add(subscribe, check)
    await message.answer_photo(caption=sendText, photo=sendImg, reply_markup=keyboard)
    await States.USER_SUBSCRIBE.set()


async def checkSubscribe(call:types.CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id=channel, user_id=call.from_user.id)
    if user_channel_status["status"] == 'left':
        return await call.answer("Вы не подписаны на канал")
    
    await bot.send_message(chat_id=sendNotificationId, text = f"@{call.from_user.username} подписался")
    
    with open(Path("utils","messageContent","messageAfterFirstMessage","sendImg.txt"), "r", encoding="utf-8") as imgFile:
        sendImg = imgFile.read()

    with open(Path("utils","messageContent","messageAfterFirstMessage","sendText.txt"), "r", encoding="utf-8") as textFile:
        sendText = textFile.read()

    view = InlineKeyboardButton("Смотреть", callback_data = "view")
    keyboard = InlineKeyboardMarkup(row_width=1).add(view)
    await call.message.answer_photo(caption=sendText, photo=sendImg, reply_markup = keyboard)

    await States.USER_VIEW.set()


    
    



    
    