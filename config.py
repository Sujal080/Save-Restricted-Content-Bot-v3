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

API_ID = os.getenv("API_ID", "25933223")
API_HASH = os.getenv("API_HASH", "6ef5a426d85b7f01562a41e6416791d3")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8011258851:AAG7gJ3QTIfTv_ERwX9IS81DAkab_2cHrhY")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://Sujalbot:Sujal123@cluster0.psoqeoy.mongodb.net/")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "8118667253").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "Sujalbot")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002799217873")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002799217873")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/+VZXbQJx9UgZjOWNl") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/Xyzaxvn")

