import time
import platform
from datetime import datetime

import pyrogram
import telethon
import motor
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from telegram import __version__ as ptb_version

from AloneMusic import app
from AloneMusic.core.call import Alone
from AloneMusic.utils import bot_sys_stats
from AloneMusic.utils.decorators.language import language
from config import BANNED_USERS, PING_IMG_URL, BOT_VERSION, SUPPORT_CHAT, OWNER_ID

@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client: pyrogram.Client, message: Message, _):
    start_time = time.time()
    
    # 1. Send initial "checking" photo
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )

    # 2. Fetch System Metrics
    # Using your existing utility for UP, CPU, RAM, and Disk
    try:
        pytgping = await Alone.ping()
        UP, CPU, RAM, DISK = await bot_sys_stats()
    except Exception:
        # Fallback if stats utility fails
        UP, CPU, RAM, DISK = "Unknown", "0%", "0%", "0%"
    
    # 3. Calculate Response Latency
    end_time = time.time()
    resp_ms = round((end_time - start_time) * 1000, 2)

    # 4. Premium Reworded Text
    alive_text = (
        f"**╭───────────────**\n"
        f"**│ ✧ {app.mention} Sᴛᴀᴛᴜs ✧**\n"
        f"**╰───────────────**\n\n"
        f"**🚀 Lᴀᴛᴇɴᴄʏ ➛** `{resp_ms} ms`\n"
        f"**⏳ Uᴘᴛɪᴍᴇ ➛** `{UP}`\n\n"
        f"**📊 Sʏsᴛᴇᴍ Rᴇsᴏᴜʀᴄᴇs:**\n"
        f"**✨ CPU ➛** `{CPU}`\n"
        f"**✨ RAM ➛** `{RAM}`\n"
        f"**✨ Dɪsᴋ ➛** `{DISK}`\n\n"
        f"**📢 Nᴏᴛᴇs:**\n"
        f"Sʏsᴛᴇᴍs ᴀʀᴇ ᴏᴘᴇʀᴀᴛɪᴏɴᴀʟ ᴀɴᴅ ʀᴇᴀᴅʏ ᴛᴏ ᴠɪʙᴇ! 🔊"
    )

    # 5. Sleek Navigation Buttons
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✨ Sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
            InlineKeyboardButton("🛠️ Sᴛᴀᴄᴋ", callback_data="version_info")
        ],
        [
            InlineKeyboardButton("👑 Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID)
        ]
    ])

    # 6. Edit the caption with full details
    await response.edit_text(
        alive_text,
        reply_markup=buttons
    )

@app.on_callback_query(filters.regex("version_info"))
async def callback_query_handler(client: pyrogram.Client, callback_query):
    # Dynamic library version fetching
    try:
        version_info = (
            f"🎨 Bᴏᴛ Vᴇʀsɪᴏɴ: {BOT_VERSION}\n"
            f"────────────────────\n"
            f"📱 Pʏʀᴏɢʀᴀᴍ: {pyrogram.__version__}\n"
            f"📡 Tᴇʟᴇᴛʜᴏɴ: {telethon.__version__}\n"
            f"🤖 PTB: {ptb_version}\n"
            f"🗄️ Mᴏᴛᴏʀ: {motor.version}\n"
            f"🐍 Pʏᴛʜᴏɴ: {platform.python_version()}"
        )
    except Exception as e:
        version_info = f"Error fetching versions: {str(e)}"

    await callback_query.answer(
        version_info,
        show_alert=True
    )
