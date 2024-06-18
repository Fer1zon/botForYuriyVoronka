from aiogram.dispatcher import Dispatcher



import sys
import os


sys.path.append(os.path.dirname(__file__) + '/..')
from handlers.startBotHandlers.startBotHandlerAdmin import startBotHandlerAdmin
from handlers.startBotHandlers.startBotHandlerUser import startBotHandlerUser, checkSubscribe
from importantFiles.helps import States, dp,bot, cur,conn

from importantFiles.config import adminId

from aiogram import types

from handlers.otherHandlers.mainOtherHandler import getPhotoId, getVideoId, getVoiceId

from handlers.userHandlers.mainUserHandler import viewContent



def registerStartHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к началу пользования ботом
    dp.register_message_handler(startBotHandlerUser, commands="start")
    dp.register_message_handler(startBotHandlerAdmin, commands="start")
    



def registerOtherHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к прочему(Выходы, бэки и тп)
    dp.register_message_handler(getPhotoId, content_types=types.ContentType.PHOTO, state = "*")
    dp.register_message_handler(getVideoId, content_types=types.ContentType.VIDEO, state = "*")
    dp.register_message_handler(getVoiceId, content_types=types.ContentType.VOICE, state = "*")


def registerUserHandler(dp:Dispatcher):#Регистрация юзерских хандлеров
    dp.register_callback_query_handler(checkSubscribe, lambda call: call.data == "check", state = States.USER_SUBSCRIBE)
    dp.register_callback_query_handler(viewContent, lambda call: call.data == "view", state = States.USER_VIEW)




def registerAdminHandler(dp:Dispatcher):#Регистрация админ хандлеров
    pass





def finalHandlerRegistrator(dp:Dispatcher):#Функция для регистрации всего, и дальнейшего его использования в launch.py
    registerStartHandler(dp)
    registerUserHandler(dp)
    registerAdminHandler(dp)
    registerOtherHandler(dp)