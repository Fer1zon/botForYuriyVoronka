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

from appShedulerFunc.Sample import scheduler, sendPodcast

from asyncio import sleep




async def paidClick(call:types.CallbackQuery, state:FSMContext):
    await sleep(1)
    
    await state.update_data(payStatus = "True")

    async with state.proxy() as data:
        gettingPodcast = data["gettingPodcast"]


    await state.update_data(gettingPodcast = "True")


    


    sendText = f"""
Спасибо. Информация для подключения у вас на почте
"""
    
    await call.message.answer(sendText)

    scheduler.add_job(sendPodcast, "date", run_date = datetime.now() + timedelta(hours=3), args=[call.from_user.id])
    #scheduler.add_job(sendPodcast, "date", run_date = datetime.now() + timedelta(seconds=15), args=[call.from_user.id, "True", gettingPodcast])



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



    

