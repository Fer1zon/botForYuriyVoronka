from aiogram.dispatcher import Dispatcher



import sys
import os


sys.path.append(os.path.dirname(__file__) + '/..')
from handlers.startBotHandlers.startBotHandlerAdmin import startBotHandlerAdmin
from handlers.startBotHandlers.startBotHandlerUser import startBotHandlerUser, checkSubscribe
from importantFiles.helps import States, dp,bot, cur,conn

from importantFiles.config import adminId

from aiogram import types

from handlers.otherHandlers.mainOtherHandler import getPhotoId, getVideoId, getVoiceId, getAudioId

from handlers.userHandlers.mainUserHandler import viewContent, message2, message3, askQuestion, sendQuestion
from handlers.userHandlers.pay import paidClick, getPayImg





from handlers.adminHandlers.mainAdminHandler import editAudio, editImg, editVideo, editText, editHelloImg, editPodcast, editReminderVideo, editUrl1, editUrl2, editUrl3, editUrl4, editImg0, editText0, editText2, editText3, editThanksText, editVideo2, editVideo3, editText1, editVideo1, acceptApplication, declineApplication, editPodcastTextNotPay, editPodcastTextPay, editHelloText



def registerStartHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к началу пользования ботом
    dp.register_message_handler(startBotHandlerAdmin,lambda msg: msg.from_user.id in adminId,  commands=["start", "help"], state = "*")
    dp.register_message_handler(startBotHandlerUser, commands="start", state = "*")
    
    



def registerOtherHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к прочему(Выходы, бэки и тп)
    dp.register_message_handler(getPhotoId, lambda msg: msg.from_user.id in adminId, content_types=types.ContentType.PHOTO, state = "*")
    dp.register_message_handler(getVideoId, lambda msg: msg.from_user.id in adminId, content_types=types.ContentType.VIDEO, state = "*")
    dp.register_message_handler(getVoiceId, lambda msg: msg.from_user.id in adminId, content_types=types.ContentType.VOICE, state = "*")
    dp.register_message_handler(getAudioId, lambda msg: msg.from_user.id in adminId, content_types=types.ContentType.AUDIO, state = "*")


def registerUserHandler(dp:Dispatcher):#Регистрация юзерских хандлеров
    dp.register_callback_query_handler(checkSubscribe, lambda call: call.data == "check", state = States.USER_SUBSCRIBE)
    dp.register_callback_query_handler(viewContent, lambda call: call.data == "view", state = States.USER_VIEW)
    dp.register_callback_query_handler(message2, lambda call: call.data.split("|")[0] == "nextMessage2", state = States.USER_MESSAGE_1)
    dp.register_callback_query_handler(message3, lambda call: call.data.split("|")[0] == "nextMessage3", state = States.USER_MESSAGE_2)

    dp.register_callback_query_handler(paidClick, lambda call: call.data == "paid", state = [States.USER_MESSAGE_3, States.GET_PAY_IMG])
    dp.register_message_handler(getPayImg, content_types="photo", state = States.GET_PAY_IMG)

    dp.register_callback_query_handler(askQuestion, lambda call: call.data == "askQuestion", state = States.USER_MESSAGE_3)
    dp.register_message_handler(sendQuestion, content_types="text", state=States.USER_ASK_QUESTION)




def registerAdminHandler(dp:Dispatcher):#Регистрация админ хандлеров
    dp.register_message_handler(editHelloImg, commands="edit_hello_img", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editHelloText, commands="edit_hello_text", state = States.ADMIN_MAIN_MENU)

    dp.register_message_handler(editText0, commands="edit_text_0", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editImg0, commands="edit_img_0", state = States.ADMIN_MAIN_MENU)
    
    dp.register_message_handler(editText1, commands="edit_text_1", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editVideo1, commands="edit_video_1", state = States.ADMIN_MAIN_MENU)
    
    dp.register_message_handler(editText2, commands="edit_text_2", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editVideo2, commands="edit_video_2", state = States.ADMIN_MAIN_MENU)
    
    dp.register_message_handler(editText3, commands="edit_text_3", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editVideo3, commands="edit_video_3", state = States.ADMIN_MAIN_MENU)

    dp.register_message_handler(editUrl1, commands="edit_url_1", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editUrl2, commands="edit_url_2", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editUrl3, commands="edit_url_3", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editUrl4, commands="edit_url_4", state = States.ADMIN_MAIN_MENU)

    dp.register_message_handler(editThanksText, commands="edit_thanks_text", state = States.ADMIN_MAIN_MENU)

    dp.register_message_handler(editPodcast, commands="edit_podcast", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editPodcastTextNotPay, commands="edit_podcast_text_not_pay", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(editPodcastTextPay, commands="edit_podcast_text_pay", state = States.ADMIN_MAIN_MENU)

    dp.register_message_handler(editReminderVideo, commands="edit_reminder", state = States.ADMIN_MAIN_MENU)


    dp.register_message_handler(editVideo, content_types="video", state = States.ADMIN_VIDEO)
    dp.register_message_handler(editAudio, content_types="audio", state = States.ADMIN_AUDIO)
    dp.register_message_handler(editImg, content_types="photo", state = States.ADMIN_IMG)


    dp.register_callback_query_handler(acceptApplication, lambda call: call.data.split("|")[0] == "accept", state = "*")
    dp.register_callback_query_handler(declineApplication, lambda call: call.data.split("|")[0] == "decline", state = "*")



def finalHandlerRegistrator(dp:Dispatcher):#Функция для регистрации всего, и дальнейшего его использования в launch.py
    registerStartHandler(dp)
    registerUserHandler(dp)
    registerAdminHandler(dp)
    registerOtherHandler(dp)