#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "7044734"))
API_HASH = environ.get("API_HASH", "3042441d631955272db1358e1d37fefb")
BOT_TOKEN = environ.get("BOT_TOKEN", "1985315401:AAHmoSddt70pcIcu7nur8xY734wTpnhxYUk")

OWNER = int(environ.get("OWNER", "1849310921"))
CREDIT = environ.get("CREDIT", "GROUP ADMIN")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1849310921').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1849310921').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


