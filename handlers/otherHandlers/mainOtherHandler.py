from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn


async def getPhotoId(message:types.Message):
    await message.answer(message.photo[-1].file_id)

async def getVideoId(message:types.Message):
    await message.answer(message.video.file_id)

async def getVoiceId(message:types.Message):
    await message.answer(message.voice.file_id)
