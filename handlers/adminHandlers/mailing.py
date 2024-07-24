
from aiogram import types

from aiogram.dispatcher import FSMContext



import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn
from utils.function.database.users import getAllUsers
from asyncio import sleep


async def sendResult(userId : int):
    state: FSMContext = dp.current_state(chat=userId, user=userId)
    async with state.proxy() as data:
        text = data["text"]
        content = data["content"]

    if text == None and content == None:
        return
    
    elif text != None and content == None:
        await bot.send_message(userId, text)

    elif text == None and content != None:
        if content["type"] == "photo":
            await bot.send_photo(userId, content["content"])

        elif content["type"] == "video":
            await bot.send_video(userId, content["content"])

        elif content["type"] == "voice":
            await bot.send_voice(userId, content["content"])

    elif text != None and content != None:
        

        if content["type"] == "photo":
            await bot.send_photo(userId, content["content"])

        elif content["type"] == "video":
            await bot.send_video(userId, content["content"])

        elif content["type"] == "voice":
            await bot.send_voice(userId, content["content"])

        await bot.send_message(userId, text)



async def sendMessageToUser(userId, text, content):
    if text == None and content == None:
        return
    
    elif text != None and content == None:
        await bot.send_message(userId, text)

    elif text == None and content != None:
        if content["type"] == "photo":
            await bot.send_photo(userId, content["content"])

        elif content["type"] == "video":
            await bot.send_video(userId, content["content"])

        elif content["type"] == "voice":
            await bot.send_voice(userId, content["content"])

    elif text != None and content != None:
        

        if content["type"] == "photo":
            await bot.send_photo(userId, content["content"])

        elif content["type"] == "video":
            await bot.send_video(userId, content["content"])

        elif content["type"] == "voice":
            await bot.send_voice(userId, content["content"])

        await bot.send_message(userId, text)


        


async def getTextMailing(message:types.Message, state:FSMContext):
    if len(message.text) > 4096:
        return await message.answer("Текст не должен превышать 4096 символов!")
    

    await state.update_data(text = message.text)

    await sendResult(message.from_user.id)


async def getPhotoMailing(message:types.Message, state:FSMContext):
    photo = message.photo[-1].file_id

    await state.update_data(content = {"type" : "photo", "content" : photo})

    await sendResult(message.from_user.id)


async def getVideoMailing(message:types.Message, state:FSMContext):
    video = message.video.file_id

    await state.update_data(content = {"type" : "video", "content" : video})

    await sendResult(message.from_user.id)

async def getVoiceMailing(message:types.Message, state:FSMContext):
    voice = message.voice.file_id

    await state.update_data(content = {"type" : "voice", "content" : voice})

    await sendResult(message.from_user.id)





async def startMailing(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        text = data["text"]
        content = data["content"]

    if text == None and content == None:
        return await message.answer("Вы не указали текст или контент для рассылки!")
    
    await message.answer("Рассылка началась. Как только она завершиться, я сообщу вам.")
    await message.answer("Вы в меню")
    await States.ADMIN_MAIN_MENU.set()
    i = 0
    for data in getAllUsers(cur):
        id = data[0]
        try:
            await sendMessageToUser(id, text, content)
        
        except:
            pass
        i += 1

        if i >= 5:
            i = 0
            await sleep(6)
            continue

    await message.answer("Рассылка завершена")

    
    





