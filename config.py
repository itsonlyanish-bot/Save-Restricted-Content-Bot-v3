# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "34734487")
API_HASH = os.getenv("API_HASH", "648191684a5c39cbc2827ea0d82bc382")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7776113950:AAFuWyGTv7vaz87t0d6vQi3JkJU1CL5KFXA")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://luckykumar7004816_db_user:JDqDFZOt35wcxqkq@cluster0.urztudy.mongodb.net/?appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("-1006737662463", "").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "savefromrestricted")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1003049395595")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1003052622136")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "100"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "1000"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/savefromrestricted") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/savefromrestricted")





