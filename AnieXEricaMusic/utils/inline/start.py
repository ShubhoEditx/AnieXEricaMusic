from pyrogram.types import InlineKeyboardButton

import config
from AnieXEricaMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="♡𝐀ᴅᴅ 𝐌ᴇ 𝐈ɴ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴏ♡",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝐆ʀᴏᴜᴘ ♡", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝐌ᴏʀᴇ ♡", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="𝐒ʜᴜʙʜᴏ ♡",
                url=f"https://t.me/Chini_tomare",
            ),
            InlineKeyboardButton(
                text="𝐒ᴏʜɪɴɪ ♡",
                url=f"https://t.me/cheynos_amare",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐅ᴇᴀᴛᴜʀᴇs ♡", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons
