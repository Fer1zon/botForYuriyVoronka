from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta


from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta


from importantFiles.helps import bot





async def sendCircularVideo(chat_id, video_id):
    await bot.send_video(chat_id, video_id)
    
    





scheduler = AsyncIOScheduler({
    
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///importantFiles/dataBase/data_base.db'
    }
})
