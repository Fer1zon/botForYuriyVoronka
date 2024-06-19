from datetime import datetime, timedelta
from aiogram import types

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from pathlib import Path

from validators import url

import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn
from appShedulerFunc.Sample import sendPodcast, scheduler


async def acceptApplication(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer("Заявка принята")

    

    userId = call.data.split("|")[1]
    # state: FSMContext = dp.current_state(chat=userId, user=userId)
    

    with open(Path("utils","messageContent","thanksForPay.txt"), "r", encoding="utf-8") as textFile:
        sendUserText = textFile.read()

    await bot.send_message(chat_id=userId, text=sendUserText)
    # scheduler.add_job(sendPodcast, "date", run_date = datetime.now() + timedelta(hours=3), args=[userId])
    scheduler.add_job(sendPodcast, "date", run_date = datetime.now() + timedelta(seconds=20), args=[userId])

async def declineApplication(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer("Заявка отклонена")

    userId = call.data.split("|")[1]
    state: FSMContext = dp.current_state(chat=userId, user=userId)

    await state.update_data(payStatus = "False")

    sendUserText = "Ваша заявка отклонена"

    await bot.send_message(chat_id=userId, text=sendUserText)



async def editHelloImg(message : types.message, state:FSMContext):
    await state.update_data(imgPath = Path("utils","messageContent","startMessageContent","imgStartMessage.txt"))
    await message.answer("Отправьте изображение")
    await States.ADMIN_IMG.set()



async def editText0(message : types.message, state:FSMContext):
    if len(message.get_args()) == 0:
        return await message.answer("Вы не указали текст")
    
    with open(Path("utils","messageContent","messageAfterFirstMessage","sendText.txt"), "w", encoding="utf-8") as textFile:
        textFile.write(message.get_args())
    await message.answer("Текст успешно изменён")
    

async def editImg0(message : types.message, state:FSMContext):
    await state.update_data(imgPath = Path("utils","messageContent","messageAfterFirstMessage","sendImg.txt"))
    await message.answer("Отправьте изображение")
    await States.ADMIN_IMG.set()



async def editText1(message : types.message, state:FSMContext):
    if len(message.get_args()) == 0:
        return await message.answer("Вы не указали текст")
    
    with open(Path("utils","messageContent","message1","sendText.txt"), "w", encoding="utf-8") as textFile:
        textFile.write(message.get_args())

    await message.answer("Текст успешно изменён")

async def editVideo1(message : types.message, state:FSMContext):
    await state.update_data(videoPath = Path("utils","messageContent","message1","sendVideo.txt"))
    await message.answer("Отправьте видео")
    await States.ADMIN_VIDEO.set()


async def editText2(message : types.message, state:FSMContext):
    if len(message.get_args()) == 0:
        return await message.answer("Вы не указали текст")
    
    with open(Path("utils","messageContent","message2","sendText.txt"), "w", encoding="utf-8") as textFile:
        textFile.write(message.get_args())
        
    await message.answer("Текст успешно изменён")

async def editVideo2(message : types.message, state:FSMContext):
    await state.update_data(videoPath = Path("utils","messageContent","message2","sendVideo.txt"))
    await message.answer("Отправьте видео")
    await States.ADMIN_VIDEO.set()


async def editText3(message : types.message, state:FSMContext):
    if len(message.get_args()) == 0:
        return await message.answer("Вы не указали текст")
    
    with open(Path("utils","messageContent","message3","sendText.txt"), "w", encoding="utf-8") as textFile:
        textFile.write(message.get_args())

    await message.answer("Текст успешно изменён")

async def editVideo3(message : types.message, state:FSMContext):
    await state.update_data(videoPath = Path("utils","messageContent","message1","sendVideo.txt"))
    await message.answer("Отправьте видео")
    await States.ADMIN_VIDEO.set()



async def editUrl1(message : types.message):
    if len(message.get_args()) == 0:
        return await message.answer("Вы не указали ссылку")
    
    if not url(message.get_args()):
        return await message.answer("Вы ввели не валидную ссылку")
    

    with open(Path("utils","messageContent","payUrl","9990.txt"), "w", encoding="utf-8") as textFile:
        textFile.write(message.get_args())

    await message.answer("Ссылка успешно изменена")

async def editUrl2(message : types.message):
    if len(message.get_args()) == 0:
        return await message.answer("Вы не указали ссылку")
    
    if not url(message.get_args()):
        return await message.answer("Вы ввели не валидную ссылку")
    
    
    with open(Path("utils","messageContent","payUrl","54990.txt"), "w", encoding="utf-8") as textFile:
        textFile.write(message.get_args())

    await message.answer("Ссылка успешно изменена")


async def editUrl3(message : types.message):
    if len(message.get_args()) == 0:
        return await message.answer("Вы не указали ссылку")
    
    if not url(message.get_args()):
        return await message.answer("Вы ввели не валидную ссылку")
    
    
    with open(Path("utils","messageContent","payUrl","10990.txt"), "w", encoding="utf-8") as textFile:
        textFile.write(message.get_args())

    await message.answer("Ссылка успешно изменена")


async def editUrl4(message : types.message):
    if len(message.get_args()) == 0:
        return await message.answer("Вы не указали ссылку")
    
    if not url(message.get_args()):
        return await message.answer("Вы ввели не валидную ссылку")
    
    
    with open(Path("utils","messageContent","payUrl","39990.txt"), "w", encoding="utf-8") as textFile:
        textFile.write(message.get_args())

    await message.answer("Ссылка успешно изменена")


async def editThanksText(message : types.message):
    if len(message.get_args()) == 0:
        return await message.answer("Вы не указали текст")
    
    with open(Path("utils","messageContent","thanksForPay.txt"), "w", encoding="utf-8") as textFile:
        textFile.write(message.get_args())


    await message.answer("Текст успешно изменён")


async def editPodcast(message : types.message, state:FSMContext):
    await state.update_data(audioPath = Path("utils","messageContent","podcastWithStudent","audio.txt"))
    await message.answer("Отправьте аудиофайл")
    await States.ADMIN_AUDIO.set()


async def editReminderVideo(message : types.message, state:FSMContext):
    await state.update_data(videoPath = Path("utils","messageContent","circularMessage","video.txt"))
    await message.answer("Отправьте видео")
    await States.ADMIN_VIDEO.set()





































async def editText(message : types.message, state:FSMContext):
    async with state.proxy() as data:
        textPath = data["textPath"]
    
    with open(textPath, "w", encoding = "utf-8") as text:
        text.write(message.text)

    await message.answer("Текст изменен")
    await States.ADMIN_MAIN_MENU.set()


async def editVideo(message : types.message, state:FSMContext):
    async with state.proxy() as data:
        videoPath = data["videoPath"]

    with open(videoPath, "w", encoding = "utf-8") as video:
        video.write(message.video.file_id)

    await message.answer("Видео изменено")
    await States.ADMIN_MAIN_MENU.set()

async def editAudio(message : types.message, state:FSMContext):
    async with state.proxy() as data:
        audioPath = data["audioPath"]

    with open(audioPath, "w", encoding = "utf-8") as audio:
        audio.write(message.audio.file_id)

    await message.answer("Аудио изменено")
    await States.ADMIN_MAIN_MENU.set()

async def editImg(message : types.message, state:FSMContext):
    async with state.proxy() as data:
        imgPath = data["imgPath"]
    
    with open(imgPath, "w", encoding = "utf-8") as img:
        img.write(message.photo[-1].file_id)

    await message.answer("Изображение изменено")
    await States.ADMIN_MAIN_MENU.set()













