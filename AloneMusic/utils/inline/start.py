from pyrogram.types import InlineKeyboardButton
import config
from AloneMusic import app

def start_panel(_):
    # Fetching values dynamically
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
                text="🎶 ᴍᴜsɪᴄ", 
                callback_data="Music_"
            ),
            InlineKeyboardButton(
                text="ℹ️ ʜᴇʟᴘ & ᴄᴍᴅs", 
                callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="📞 sᴜᴘᴘᴏʀᴛ", 
                url=f"{support_chat}"
            ),
            InlineKeyboardButton(
                text="🔔 ᴜᴘᴅᴀᴛᴇs", 
                url="https://t.me/pookie_updates"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👑 ᴏᴡɴᴇʀ", 
                url="https://t.me/NottyBcha"
            ),
        ],
    ]
    return buttons
