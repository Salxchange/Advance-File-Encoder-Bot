from time import sleep
import humanize
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import db
from script import Txt



@Client.on_message((filters.private | filters.group) & filters.command('start'))
async def Handle_StartMsg(bot:Client, msg:Message):

    Snowdev = await msg.reply_text(text= '**Please Wait...**', reply_to_message_id=msg.id)

    if msg.chat.type == enums.ChatType.SUPERGROUP and not db.is_user_exist(msg.from_user.id):
        botusername = await bot.get_me()
        btn = [
            [InlineKeyboardButton(text='⚡ BOT PM', url=f'https://t.me/{botusername.username}')],
            [InlineKeyboardButton(text='💻 Dᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Snowball_Official')]
        ]

        await Snowdev.edit(text=Txt.GROUP_START_MSG.format(msg.from_user.mention), reply_markup=InlineKeyboardMarkup(btn))
    
    else:
        btn = [
            [InlineKeyboardButton(text='❗ Hᴇʟᴘ', callback_data='help'), InlineKeyboardButton(text='🌨️ Aʙᴏᴜᴛ', callback_data='about')],
            [InlineKeyboardButton(text='📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/AIORFT'), InlineKeyboardButton(text='💻 Dᴇᴠᴇʟᴏᴘᴇʀ', callback_data='https://t.me/Snowball_Official')]
        ]

        await Snowdev.edit(text=Txt.PRIVATE_START_MSG.format(msg.from_user.mention), reply_markup=InlineKeyboardMarkup(btn))
    

@Client.on_message((filters.private | filters.group) & (filters.document | filters.audio | filters.video))
async def Files_Option(bot:Client, message:Message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    
    
    SnowDev = await message.reply_text(text='**Please Wait**', reply_to_message_id=message.id)

    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 RENAME 📝", callback_data="rename")],
                   [InlineKeyboardButton("🗜️ COMPRESS 🗜️", callback_data="compress")]]
        await SnowDev.edit(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 RENAME 📝", callback_data="rename")],
                   [InlineKeyboardButton("🗜️ COMPRESS 🗜️", callback_data="compress")]]
        await SnowDev.edit(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    except Exception as e:
        print(e)


