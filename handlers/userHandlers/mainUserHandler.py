from aiogram import types

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from pathlib import Path
from datetime import datetime, timedelta

import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from appShedulerFunc.Sample import scheduler, sendCircularVideo, editMessageAfter3Hours, sendMessageAfter6Hours, sendPodcast

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.userHandlers import keyboard as kb

from importantFiles.config import sendNotificationId

from asyncio import sleep


async def viewContent(call:types.CallbackQuery):
    
    await call.message.edit_reply_markup(reply_markup=None)
    await sleep(2)


    with open(Path("utils","messageContent","message1","sendText.txt"), "r", encoding="utf-8") as textFile:
        sendText = textFile.read()

    with open(Path("utils","messageContent","message1","sendVideo.txt"), "r", encoding="utf-8") as videoFile:
        sendVideo = videoFile.read()

    with open(Path("utils","messageContent","circularMessage","video.txt"), "r", encoding="utf-8") as videoFile1:
        sendVideo1 = videoFile1.read()

    job_id = f"{call.from_user.id}CircularVideo"

    nextButton = InlineKeyboardButton("Смотреть дальше ⏩", callback_data = "nextMessage2|" + job_id)
    keyboard = InlineKeyboardMarkup().add(nextButton)

    #scheduler.add_job(sendCircularVideo, "date", run_date = datetime.now() + timedelta(seconds=20), id = job_id, args=[call.from_user.id, sendVideo1])
    scheduler.add_job(sendCircularVideo, "date", run_date = datetime.now() + timedelta(minutes=20), id = job_id, replace_existing=True, args=[call.from_user.id, sendVideo1])
    
    await call.message.answer_video(caption=sendText, video=sendVideo, reply_markup=keyboard)
    await States.USER_MESSAGE_1.set()


async def message2(call:types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await sleep(2)
    try:#Удаление прошлой задачи если она существует
        deleteJobId = call.data.split("|")[1]
        scheduler.remove_job(deleteJobId)
    except:
        pass


    with open(Path("utils","messageContent","message2","sendText.txt"), "r", encoding="utf-8") as textFile:
        sendText = textFile.read()

    with open(Path("utils","messageContent","message2","sendVideo.txt"), "r", encoding="utf-8") as videoFile:
        sendVideo = videoFile.read()

    with open(Path("utils","messageContent","circularMessage","video.txt"), "r", encoding="utf-8") as videoFile1:
        sendVideo1 = videoFile1.read()


    job_id = f"{call.from_user.id}CircularVideo"

    nextButton = InlineKeyboardButton("Смотреть дальше ⏩", callback_data = "nextMessage3|" + job_id)
    keyboard = InlineKeyboardMarkup().add(nextButton)

    #scheduler.add_job(sendCircularVideo, "date", run_date = datetime.now() + timedelta(seconds=20), id = job_id, args=[call.from_user.id, sendVideo1])
    scheduler.add_job(sendCircularVideo, "date", run_date = datetime.now() + timedelta(minutes=20), id = job_id, replace_existing=True, args=[call.from_user.id, sendVideo1])
    
    await call.message.answer_video(caption=sendText, video=sendVideo, reply_markup=keyboard)
    await States.USER_MESSAGE_2.set()


async def message3(call:types.CallbackQuery, state:FSMContext):
    await call.message.edit_reply_markup(reply_markup=None)
    await sleep(2)
    
    await state.update_data(payStatus = "False")
    try:#Удаление прошлой задачи если она существует
        deleteJobId = call.data.split("|")[1]
        scheduler.remove_job(deleteJobId)
    except:
        pass


    with open(Path("utils","messageContent","message3","sendText.txt"), "r", encoding="utf-8") as textFile:
        sendText = textFile.read()

    with open(Path("utils","messageContent","message3","sendVideo.txt"), "r", encoding="utf-8") as videoFile:
        sendVideo = videoFile.read()


    with open(Path("utils","messageContent","payUrl","url1.txt"), encoding="utf-8") as urlFile:
        url = urlFile.read()

    tariff = InlineKeyboardButton("Тариф «Халява» 🤑", url=url)
    keyboard = InlineKeyboardMarkup(row_width=1).add(tariff, kb.paid, kb.askQuestion)

    msg = await call.message.answer_video(caption=sendText, video=sendVideo, reply_markup=keyboard)

    #scheduler.add_job(editMessageAfter3Hours, "date", run_date = datetime.now() + timedelta(seconds=20), args=[call.from_user.id, msg.message_id, state])
    scheduler.add_job(editMessageAfter3Hours, "date", run_date = datetime.now() + timedelta(hours=3), args=[call.from_user.id, msg.message_id, state])

    scheduler.add_job(sendMessageAfter6Hours, "date", run_date = datetime.now() + timedelta(hours = 6), args=[call.from_user.id, state, msg.message_id, []])
    #scheduler.add_job(sendMessageAfter6Hours, "date", run_date = datetime.now() + timedelta(seconds=20), args=[call.from_user.id, state, msg.message_id, []])

    
    await States.USER_MESSAGE_3.set()



async def askQuestion(call:types.CallbackQuery):
    await call.message.answer("Какой у вас вопрос?")
    await States.USER_ASK_QUESTION.set()

    await sleep(2 * 60)
    
    await States.USER_MESSAGE_3.set()



async def sendQuestion(message:types.Message):
    await message.answer("Спасибо за ваш вопрос. Мы обязательно ответим вам в ближайшее время.")
    await States.USER_MESSAGE_3.set()

    sendText = f"""
<b>Вопрос от пользователя</b> @{message.from_user.username}:
{message.text}"""

    await bot.send_message(chat_id=sendNotificationId, text=sendText)
