# (C) 2021 Jayant Kageri

from pyrogram import idle, Client, filters
from _pyrogram import app, LOGGER
from _pyrogram.modules import *
import os
import asyncio

print("Pyrogram User Client is Start")
app.start()
print(app.get_me)
loop = asyncio.get_event_loop()
loop.run_forever()    
