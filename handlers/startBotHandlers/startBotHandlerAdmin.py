
from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State

import sys 
import os 

from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn


async def startBotHandlerAdmin(message : types.message):
    with open(Path("utils", "messageContent", "adminCommands.txt"), "r", encoding = "utf-8") as textFile:
        sendText = textFile.read()

    await message.answer(sendText)
    await States.ADMIN_MAIN_MENU.set()
