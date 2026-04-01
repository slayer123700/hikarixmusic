#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton
import config
from AloneMusic import app

def start_panel(_):
    # Using config variables or app username dynamically
    # Ensure these are defined in your config.py
    bot_username = app.username
    support_chat = config.SUPPORT_CHAT
    
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{bot_username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ℹ️ ʜᴇʟᴘ & ᴄᴍᴅs", 
                callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="🎵 ᴍᴜsɪᴄ", 
                callback_data="Music_"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✨ sᴜᴘᴘᴏʀᴛ", 
                url=f"{support_chat}"
            ),
            InlineKeyboardButton(
                text="📢 ᴜᴘᴅᴀᴛᴇs", 
                url="https://t.me/pookie_updates"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❄️ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", 
                url="https://github.com/RolexXd/hikarixmusic"
            ),
            InlineKeyboardButton(
                text="👑 ᴏᴡɴᴇʀ", 
                url="https://t.me/billichor"
            ),
        ],
    ]
    return buttons
