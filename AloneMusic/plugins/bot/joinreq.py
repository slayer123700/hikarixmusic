from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ChatJoinRequest,
    CallbackQuery
)
from pyrogram.errors import (
    UserNotParticipant,
    PeerIdInvalid,
    ChatAdminRequired
)
from pyrogram.enums import ChatMemberStatus as CMS

# Using your specific bot instance
from AloneMusic import app

# ==============================
# JOIN REQUEST PANEL
# ==============================

@app.on_chat_join_request()
async def handle_join_request(client: Client, request: ChatJoinRequest):
    user = request.from_user
    chat = request.chat

    # Sleek Action Buttons
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ ᴀᴄᴄᴇᴘᴛ", callback_data=f"accept_jr_{user.id}"),
            InlineKeyboardButton("❌ ᴅᴇᴄʟɪɴᴇ", callback_data=f"decline_jr_{user.id}")
        ]
    ])

    # Reworded Professional Text
    text = (
        f"**╭───────────────**\n"
        f"**│ ✧ Nᴇᴡ Jᴏɪɴ Rᴇǫᴜᴇsᴛ ✧**\n"
        f"**╰───────────────**\n\n"
        f"**👤 Usᴇʀ ➛** {user.mention}\n"
        f"**🆔 ID ➛** `{user.id}`\n"
        f"**💬 Gʀᴏᴜᴘ ➛** `{chat.title}`\n\n"
        f"**📢 Sᴛᴀᴛᴜs ➛** Pᴇɴᴅɪɴɢ Aᴘᴘʀᴏᴠᴀʟ... ⏳"
    )

    try:
        # Sending to the group where the request happened
        await client.send_message(
            chat.id,
            text,
            reply_markup=keyboard
        )
    except Exception:
        # Usually happens if bot isn't admin or lacks send_message perms
        pass


# ==============================
# ACCEPT / DECLINE HANDLER
# ==============================

@app.on_callback_query(filters.regex(r"^(accept|decline)_jr_"))
async def accept_decline_request(client: Client, query: CallbackQuery):
    # Safe Callback Answer
    try:
        await query.answer()
    except:
        pass

    admin_id = query.from_user.id
    chat_id = query.message.chat.id
    
    # Parse Data
    data = query.data.split("_")
    action = data[0]
    target_user_id = int(data[2])

    # 1. Admin Permission Check
    try:
        member = await client.get_chat_member(chat_id, admin_id)
        if member.status not in {CMS.OWNER, CMS.ADMINISTRATOR}:
            return await query.answer("⚠️ Oɴʟʏ Aᴅᴍɪɴs ᴄᴀɴ ᴍᴀɴᴀɢᴇ ʀᴇǫᴜᴇsᴛs!", show_alert=True)
    except Exception:
        return await query.answer("❌ Fᴀɪʟᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ Aᴅᴍɪɴ sᴛᴀᴛᴜs.", show_alert=True)

    # 2. Process Request
    try:
        if action == "accept":
            await client.approve_chat_join_request(chat_id, target_user_id)
            status_text = "✅ Aᴘᴘʀᴏᴠᴇᴅ"
            
            # Notify User in DMs
            try:
                await client.send_message(
                    target_user_id,
                    f"✨ **Cᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!**\n\nYᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ **{query.message.chat.title}** ʜᴀs ʙᴇᴇɴ **Aᴘᴘʀᴏᴠᴇᴅ**! 🥳"
                )
            except:
                pass

        else:
            await client.decline_chat_join_request(chat_id, target_user_id)
            status_text = "❌ Dᴇᴄʟɪɴᴇᴅ"

            # Notify User in DMs
            try:
                await client.send_message(
                    target_user_id,
                    f"😔 **Sᴏʀʀʏ!**\n\nYᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ **{query.message.chat.title}** ᴡᴀs **Dᴇᴄʟɪɴᴇᴅ**."
                )
            except:
                pass

        # 3. Update the Group Message
        target_user = await client.get_users(target_user_id)
        mention = target_user.mention if target_user else f"`{target_user_id}`"
        
        await query.edit_message_text(
            f"**╭───────────────**\n"
            f"**│ ✧ Rᴇǫᴜᴇsᴛ Pʀᴏᴄᴇssᴇᴅ ✧**\n"
            f"**╰───────────────**\n\n"
            f"**👤 Usᴇʀ ➛** {mention}\n"
            f"**🛠️ Aᴄᴛɪᴏɴ ➛** {status_text}\n"
            f"**👮 Bʏ ➛** {query.from_user.mention}\n\n"
            f"**✨ Sʏsᴛᴇᴍ Sʏɴᴄᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ!**"
        )

    except UserNotParticipant:
        await query.edit_message_text("⚠️ **Eʀʀᴏʀ:** Tʜɪs ʀᴇǫᴜᴇsᴛ ɴᴏ ʟᴏɴɢᴇʀ ᴇxɪsᴛs.")
    except ChatAdminRequired:
        await query.edit_message_text("⚠️ **Aᴅᴍɪɴ Eʀʀᴏʀ:** I ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴜsᴇʀs.")
    except Exception as e:
        await query.edit_message_text(f"⚠️ **Sʏsᴛᴇᴍ Eʀʀᴏʀ:** `{str(e)}`")
