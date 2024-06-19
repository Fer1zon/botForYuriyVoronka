from aiogram import types

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from pathlib import Path
from datetime import datetime, timedelta

from pathlib import Path

import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from importantFiles.config import sendNotificationId

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




async def payClick(call:types.CallbackQuery, state:FSMContext):
    await call.message.edit_reply_markup(reply_markup=None)
    await state.update_data(payStatus = "True")
    with open(Path("utils", "messageContent", "payUrl", call.data + ".txt"), "r", encoding="utf-8") as textFile:
        sendUrl = textFile.read()


    await state.update_data(price = call.data)


    sendText = f"""
Оплатите заказ по ссылке: {sendUrl}
После вернитесь в этот чат, и отправьте в чат скриншот оплаты.
"""
    
    await call.message.answer(sendText)
    await States.GET_PAY_IMG.set()



async def getPayImg(message:types.Message, state:FSMContext):
    
    await state.update_data(payStatus = "True")
    async with state.proxy() as data:
        price = data["price"]

    await message.answer("Ваша заявка отправлена. Ожидайте ответа администратора.")
    await States.USER_MESSAGE_3.set()
    sendAdminText = f"Пользователь @{message.from_user.username} оплатил заказ стоимостью {price}"
    sendImg = message.photo[-1].file_id

    accept = InlineKeyboardButton("Принять оплату", callback_data="accept" + "|" + str(message.from_user.id))
    decline = InlineKeyboardButton("Отклонить оплату", callback_data="decline" + "|" + str(message.from_user.id))

    keyboard = InlineKeyboardMarkup(row_width=2).add(accept, decline)


    await bot.send_photo(chat_id=sendNotificationId, caption = sendAdminText, photo=sendImg, reply_markup=keyboard)



    

