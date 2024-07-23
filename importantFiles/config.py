import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']
TEST_TOKEN = os.environ['TEST_TOKEN']

adminId = [5530562487, 542443518]

channel = "@millionlinere"
channelLink = "https://t.me/millionlinere"
sendNotificationId = 5530562487


dataBasePath = os.path.dirname(__file__) + '/dataBase/data_base.db'