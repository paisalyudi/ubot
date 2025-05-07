import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "99"))

DEVS = list(map(int, os.getenv("DEVS", "8074609099").split()))

API_ID = int(os.getenv("API_ID", "23608953"))

API_HASH = os.getenv("API_HASH", "253f5f31989038f81ebf234f008df79f")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7772475060:AAGFjk8XCb4mpAIVAkFEKcysYyaE5XAfvG0")

OWNER_ID = int(os.getenv("OWNER_ID", "8074609099"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002458741546").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ml9079716:48gxGsQhTHWumLI15@cluster0.6e1q9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv(" -1002458741546"))

USER_GROUP = os.getenv("USER_GROUP", "@roompublicblackderry")
