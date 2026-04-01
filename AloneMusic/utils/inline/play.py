import math
from pyrogram.types import InlineKeyboardButton
from AloneMusic import app
from AloneMusic.utils.formatters import time_to_seconds

# --- Helper for dynamic progress bar ---
def get_progress_bar(percentage):
    """Generates a sleek progress bar based on percentage."""
    # Scale 0-100 to a 10-segment bar
    index = min(math.floor(percentage / 10), 9)
    chars = ["—"] * 10
    chars[index] = "♬"
    return f"|{''.join(chars)}|"

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="🎵 Aᴜᴅɪᴏ", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎬 Vɪᴅᴇᴏ", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
    ]
    return buttons

def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)

    remaining_sec = max(0, duration_sec - played_sec)
    rem_min, rem_sec = divmod(remaining_sec, 60)
    remaining = f"{rem_min:02d}:{rem_sec:02d}"

    percentage = (played_sec / duration_sec) * 100 if duration_sec else 0
    bar = get_progress_bar(percentage)

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {remaining}",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="🔄", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="⏹", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="✨ ᴄʟᴏsᴇ ✨", callback_data="close")],
    ]
    return buttons

def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="🔄", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⏹", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="🎶 Aᴜᴅɪᴏ", callback_data=f"AlonePlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎞️ Vɪᴅᴇᴏ", callback_data=f"AlonePlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [InlineKeyboardButton(text="🗑️ ᴄʟᴏsᴇ", callback_data=f"forceclose {videoid}|{user_id}")],
    ]
    return buttons

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [InlineKeyboardButton(text="🛰️ Sᴛᴀʀᴛ Lɪᴠᴇ", callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}")],
        [InlineKeyboardButton(text="🗑️ ᴄʟᴏsᴇ", callback_data=f"forceclose {videoid}|{user_id}")],
    ]
    return buttons

def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(text="🎵 Aᴜᴅɪᴏ", callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text="🎬 Vɪᴅᴇᴏ", callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="⬅️", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text="❌", callback_data=f"forceclose {query}|{user_id}"),
            InlineKeyboardButton(text="➡️", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
    ]
    return buttons
