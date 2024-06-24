
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta

from pathlib import Path

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta


from importantFiles.helps import bot, dp

from handlers.userHandlers import keyboard as kb

from asyncio import sleep

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher import FSMContext



async def sendCircularVideo(chat_id, video_id):
    await bot.send_video(chat_id, video_id)




    
    





scheduler = AsyncIOScheduler({
    
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///importantFiles/dataBase/data_base.db'
    }
})


async def editMessageAfter3Hours(chat_id, message_id, state):
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    async with state.proxy() as data:
        payStatus = data["payStatus"]

    if payStatus == "True":
        return
    with open(Path("utils","messageContent","payUrl","url2.txt"), encoding="utf-8") as urlFile:
        url = urlFile.read()

    tariff = InlineKeyboardButton("Тариф ХАЛЯВА", url=url)
    keyboard = InlineKeyboardMarkup(row_width=1).add(tariff, kb.paid, kb.askQuestion)

    await bot.edit_message_reply_markup(chat_id, message_id=message_id, reply_markup=keyboard)


    # scheduler.add_job(editMessageAfter24Hours, "date", run_date = datetime.now() + timedelta(hours=21), args=[chat_id, message_id, state])
    scheduler.add_job(editMessageAfter24Hours, "date", run_date = datetime.now() + timedelta(seconds=30), args=[chat_id, message_id, state])
    # await sleep(30)
    await sleep(10)
    await bot.send_message(chat_id=chat_id, text = "Стоимость повышена на +1000 рублей")


async def editMessageAfter24Hours(chat_id, message_id, state):
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    async with state.proxy() as data:
        payStatus = data["payStatus"]

    if payStatus == "True":
        return
    

    with open(Path("utils","messageContent","payUrl","url3.txt"), encoding="utf-8") as urlFile:
        url = urlFile.read()

    tariff = InlineKeyboardButton("ВЫБРАТЬ ТАРИФ", url=url)
    keyboard = InlineKeyboardMarkup(row_width=1).add(tariff, kb.paid, kb.askQuestion)

    await bot.edit_message_reply_markup(chat_id, message_id=message_id, reply_markup=keyboard)



    # await sleep(30)
    await sleep(10)
    await bot.send_message(chat_id=chat_id, text = "Скидка не доступна", reply_markup=keyboard)







async def sendMessageAfter14Days(chat_id, state):
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    async with state.proxy() as data:
        payStatus = data["payStatus"]

    if payStatus == "True":
        return
    
    

    sendText = "Цена снижена до 10990 на 24 часа"

    with open(Path("utils","messageContent","payUrl","url2.txt"), encoding="utf-8") as urlFile:
        url = urlFile.read()

    tariff = InlineKeyboardButton("Тариф ХАЛЯВА", url=url)
    keyboard = InlineKeyboardMarkup(row_width=1).add(tariff, kb.paid, kb.askQuestion)

    msg = await bot.send_message(chat_id=chat_id, text=sendText, reply_markup=keyboard)

    # scheduler.add_job(deleteMessageAfter24hours, "date", run_date = datetime.now() + timedelta(hours = 24), args=[chat_id, msg.message_id, state])
    scheduler.add_job(deleteMessageAfter24hours, "date", run_date = datetime.now() + timedelta(seconds=20), args=[chat_id, msg.message_id, state])






async def deleteMessageAfter24hours(chat_id, message_id, state):
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    async with state.proxy() as data:
        payStatus = data["payStatus"]

    if payStatus == "True":
        return 
    
    await bot.delete_message(chat_id=chat_id, message_id=message_id)

    # scheduler.add_job(sendMessageAfter14Days, "date", run_date = datetime.now() + timedelta(days=30), args=[chat_id, state])
    scheduler.add_job(sendMessageAfter14Days, "date", run_date = datetime.now() + timedelta(seconds = 15), args=[chat_id, state])




async def sendMessageAfter6Hours(chat_id, state):
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    async with state.proxy() as data:
        payStatus = data["payStatus"]
        

    
    




    if payStatus == "True":
        return
    
    with open(Path("utils","messageContent","podcastWithStudent","audio.txt"), "r", encoding="UTF-8") as audioFile:
        sendAudio = audioFile.read()

    with open(Path("utils","messageContent","payUrl","url2.txt"), encoding="utf-8") as urlFile:
        url = urlFile.read()

    tariff = InlineKeyboardButton("Тариф ХАЛЯВА", url=url)
    keyboard = InlineKeyboardMarkup(row_width=1).add(tariff, kb.paid, kb.askQuestion)

    await bot.send_audio(chat_id=chat_id, audio=sendAudio, reply_markup=keyboard)

    # scheduler.add_job(sendMessageAfter14Days, "date", run_date = datetime.now + timedelta(days=14), args=[chat_id, state])
    scheduler.add_job(sendMessageAfter14Days, "date", run_date = datetime.now() + timedelta(seconds=20), args=[chat_id, state])





async def sendPodcast(chat_id):
    with open(Path("utils","messageContent","podcastWithStudent","audio.txt"), "r", encoding="UTF-8") as audioFile:
        sendAudio = audioFile.read()

    with open(Path("utils","messageContent","podcastWithStudent","sendText.txt"), "r", encoding="UTF-8") as textFile:
        sendText = textFile.read()

    

    await bot.send_audio(chat_id=chat_id, caption=sendText, audio=sendAudio)

    






