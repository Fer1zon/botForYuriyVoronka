import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']
TEST_TOKEN = os.environ['TEST_TOKEN']

adminId = [5530562487]

channel = "@TEST_CHANEL7237"
channelLink = "https://t.me/TEST_CHANEL7237"
sendNotificationId = 5530562487


dataBasePath = os.path.dirname(__file__) + '/dataBase/data_base.db'