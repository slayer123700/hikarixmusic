from pyrogram.types import InlineKeyboardButton
import config
from AloneMusic import app

def private_panel(_):
    bot_username = app.username
    
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{bot_username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(
                text="📝 ᴀʙᴏᴜᴛ", 
                callback_data="Music_"  # Or your specific about callback
            ),
            InlineKeyboardButton(
                text="💬 sᴜᴘᴘᴏʀᴛ", 
                url=config.SUPPORT_CHAT
            ),
        ],
        [
            InlineKeyboardButton(
                text="🛠️ ʜᴇʟᴘ", 
                callback_data="settings_back_helper"
            ),
        ],
    ]
    return buttons

def start_panel(_):
    return private_panel(_)
