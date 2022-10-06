import os

API_HASH = os.getenv("API_HASH")
API_ID = int(os.getenv("API_ID"))
PY_SESSION = os.getenv("PYROGRAM_SESSION")
PREFIX = os.environ.get("PREFIX", ".")
LOG_CHAT = int(os.getenv("LOG_CHAT"))
