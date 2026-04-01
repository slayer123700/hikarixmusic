import asyncio
import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from AloneMusic import app
from AloneMusic.misc import _boot_
from AloneMusic.plugins.sudo.sudoers import sudoers_list
from AloneMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AloneMusic.utils.decorators.language import LanguageStart
from AloneMusic.utils.formatters import get_readable_time
from AloneMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS, OWNER_ID
from strings import get_string

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    
    # 1. Reaction
    try:
        await message.react("🍓", big=True)
    except:
        pass

    # 2. Tactical Loading Sequence
    x = await message.reply_text("`ɪɴɪᴛɪᴀʟɪᴢɪɴɢ ꜱʏꜱᴛᴇᴍꜱ...` ")
    await asyncio.sleep(0.4)
    await x.edit_text("`> ꜱʏꜱᴛᴇᴍꜱ ᴏɴʟɪɴᴇ` ")
    await asyncio.sleep(0.4)
    await x.delete()
    await asyncio.sleep(0.2)

    # 3. Random Sticker Selection
    STICKER_FILE_ID = random.choice(config.START_STICKER_FILE_ID)
    await message.reply_cached_media(file_id=STICKER_FILE_ID)
    await asyncio.sleep(0.3)

    # 4. Deep Linking Logic (Properly Indented)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        
        # Sudo list deep link
        if name.startswith("sud"):
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴄʜᴇᴄᴋᴇᴅ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n"
                         f"<b>ᴜsᴇʀ ɪᴅ:</b> <code>{message.from_user.id}</code>\n"
                         f"<b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{message.from_user.username}",
                )
            return

        # YouTube Info deep link
        if name.startswith("inf"):
            m = await message.reply_text("🔎")
            query = (name.replace("info_", "", 1)).strip()
            results = VideosSearch(f"https://www.youtube.com/watch?v={query}", limit=1)
            next_result = await results.next()

            if next_result and "result" in next_result:
                result = next_result["result"][0]
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
                
                searched_text = _["start_6"].format(
                    title, duration, views, published, channellink, channel
                )
                key = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="ʏᴏᴜᴛᴜʙᴇ", url=link)]]
                )
                await m.delete()
                await app.send_photo(
                    chat_id=message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    reply_markup=key,
                )
                if await is_on_off(2):
                    await app.send_message(
                        chat_id=config.LOGGER_ID,
                        text=f"<b>{message.from_user.mention} ᴄʜᴇᴄᴋᴇᴅ ᴛʀᴀᴄᴋ ɪɴғᴏ.</b>\n\n"
                             f"<b>• ɪᴅᴇɴᴛɪғɪᴇʀ ⌯</b> <code>{message.from_user.id}</code>\n"
                             f"<b>• ʜᴀɴᴅʟᴇ ⌯</b> {message.from_user.username}.t.me",
                    )
            else:
                await m.edit_text("ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴛʀɪᴇᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.")
            return

    # 5. Final Start Message (Hikari - Tactical Style)
    out = private_panel(_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=(
            f"𝗜 𝗮𝗺 「 ʜɪᴋᴀʀɪ 」 ♡, 𝘆𝗼𝘂𝗿 𝘃𝗲𝗿𝘀𝗮𝘁𝗶𝗹𝗲 𝘁𝗮𝗰𝘁𝗶𝗰𝗮𝗹 𝗺𝗮𝗻𝗮𝗴𝗲𝗺𝗲𝗻𝘁 𝗯𝗼𝘁, "
            "𝗱𝗲𝘀𝗶𝗴𝗻𝗲𝗱 𝘁𝗼 𝗵𝗲𝗹𝗽 𝘆𝗼𝘂 𝘁𝗮𝗸𝗲 𝗼𝘃𝗲𝗿 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽𝘀 𝘄𝗶𝘁ʜ 𝖾𝖺𝗌𝖾 𝗎𝗌𝗂𝗇𝗀 𝗆𝗒 𝗉𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝗆𝗈𝖽𝗎𝗅𝖾𝗌 𝖺𝗇𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌!\n"
            ">\n"
            "> • 𝗦𝗲𝗮𝗺𝗹𝗲𝘀𝘀 𝗆𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍 𝗈𝖿 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌 🚀\n"
            "> • 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 𝗆𝗈𝖽𝖾𝗋𝖺𝗍𝗂𝗈𝗇 𝗍𝗈𝗈𝗅𝗌 🛡️\n"
            "> • 𝗙𝗎𝗇 𝖺𝗇𝖽 𝖾𝗇𝗀𝖺𝗀𝗂𝗇𝗀 𝖿𝖾𝖺𝗍𝗎𝗋𝖾𝗌 🎮\n"
            "✧ 𝗧𝗔𝗖𝗧𝗜𝗖𝗔𝗟 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗨𝗡𝗜𝗧 ✧ 🛡️ ║ ▸ READY\n"
            ">\n"
            "> \"𝗗𝗶𝘀𝗰𝗶𝗽𝗹𝗶𝗻𝗲 𝗙𝗼𝗿𝗴𝗲𝘀 𝘄𝗮𝗿𝗿𝗶𝗼𝗿𝘀.\" ⚔️\n"
            "> — 𝗠𝘂𝘀𝗮𝘀𝗵𝗶 ✦\n"
            "📚 𝗡𝗲𝗲𝗱 𝗛𝗲𝗹𝗽?\n"
            "𝗖𝗹𝗶𝗰ᴋ 𝗍𝗁𝖾 𝖧𝖾𝗅𝗉 𝖻𝗎𝗍𝗍𝗈𝗇 𝖻𝖾𝗅𝗈𝗐 ᴛᴏ ɢᴇᴛ ᴀʟʟ ᴅᴇᴛᴀɪʟs ✨\n"
            "✧ ᴇɴᴅ ᴏꜰ ᴛʀᴀɴꜱᴍɪꜱꜱɪᴏɴ ✧ 🌌 ║ ⬢"
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )

    if await is_on_off(2):
        await app.send_message(
            chat_id=config.LOGGER_ID,
            text=f"<b>{message.from_user.mention} sᴛᴀʀᴛᴇᴅ ʜɪᴋᴀʀɪ.</b>\n\n"
                 f"<b>• ɪᴅᴇɴᴛɪғɪᴇʀ :</b> <code>{message.from_user.id}</code>\n"
                 f"<b>• ʜᴀɴᴅʟᴇ :</b> {message.from_user.username}.t.me",
        )

@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_text(
        text=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    await add_served_chat(message.chat.id)

@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_text(
                    _["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
