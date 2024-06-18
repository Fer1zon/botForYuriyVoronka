from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State

from pathlib import Path
from datetime import datetime, timedelta

import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from appShedulerFunc.Sample import scheduler, sendCircularVideo







async def viewContent(call:types.CallbackQuery):
    with open(Path("utils","messageContent","message1","sendText.txt"), "r", encoding="utf-8") as textFile:
        sendText = textFile.read()

    with open(Path("utils","messageContent","message1","sendImg.txt"), "r", encoding="utf-8") as imgFile:
        sendImg = imgFile.read()

    with open(Path("utils","messageContent","circularMessage","video.txt"), "r", encoding="utf-8") as videoFile:
        sendVideo = videoFile.read()

    scheduler.add_job(sendCircularVideo, "date", run_date = datetime.now() + timedelta(seconds=20), id = f"{call.from_user.id}1Message", args=[call.from_user.id, sendVideo])
    
    await call.message.answer_photo(caption=sendText, photo=sendImg)


















    

