import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "5343384013").split()))

API_ID = int(os.getenv("API_ID", "26297818"))

API_HASH = os.getenv("API_HASH", "4a48374f0fd3549af86a7e5fba563b8f")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7737623053:AAEf3brYvrsvvz77tmMO8N3ngre1PSIfJ3Y")

OWNER_ID = int(os.getenv("OWNER_ID", "5343384013"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://zan:zan@cluster0.epnnx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002367286705"))

