from pyrogram.types import InlineKeyboardButton
import config
from AloneMusic import app

def private_panel(_):
    """
    Renamed from start_panel to private_panel to fix the ImportError 
    in AloneMusic/plugins/bot/settings.py
    """
    bot_username = app.username
    
    buttons = [
        [
            InlineKeyboardButton(
                text="✨ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✨",
                url=f"https://t.me/{bot_username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎵 ᴍᴜsɪᴄ", 
                callback_data="Music_"
            ),
            InlineKeyboardButton(
                text="🛠️ ʜᴇʟᴘ", 
                callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💬 sᴜᴘᴘᴏʀᴛ", 
                url=config.SUPPORT_CHAT
            ),
            InlineKeyboardButton(
                text="📢 ᴜᴘᴅᴀᴛᴇs", 
                url="https://t.me/pookie_updates"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👑 ᴅᴇᴠᴇʟᴏᴘᴇʀ", 
                url="https://t.me/NottyBcha"
            ),
        ],
    ]
    return buttons

# Keep this for backward compatibility if other files still use the old name
def start_panel(_):
    return private_panel(_)
