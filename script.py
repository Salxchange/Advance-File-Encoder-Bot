class Txt(object):

    PRIVATE_START_MSG = """
Hɪ {},

ʰᵉˡˡᵒ ᵗʰᵉʳᵉ! ⁱ'ᵐ ᵗʰᵉ ᶠⁱˡᵉ ᵐᵉᵗᵃᵈᵃᵗᵃ ᵉᵈⁱᵗᵒʳ ᵇᵒᵗ, ʰᵉʳᵉ ᵗᵒ ʰᵉˡᵖ ʸᵒᵘ ᵐᵃⁿᵃᵍᵉ ᵃⁿᵈ ᵉᵈⁱᵗ ʸᵒᵘʳ ᶠⁱˡᵉ ᵐᵉᵗᵃᵈᵃᵗᵃ ᵉᶠᶠᵒʳᵗˡᵉˢˢˡʸ. ʷⁱᵗʰ ᵐʸ ᵃˢˢⁱˢᵗᵃⁿᶜᵉ, ʸᵒᵘ ᶜᵃⁿ ᵉᵃˢⁱˡʸ ᵘᵖᵈᵃᵗᵉ, ᵐᵒᵈⁱᶠʸ, ᵃⁿᵈ ᵒʳᵍᵃⁿⁱᶻᵉ ᵗʰᵉ ᵐᵉᵗᵃᵈᵃᵗᵃ ᵒᶠ ʸᵒᵘʳ ᶠⁱˡᵉˢ. ʷʰᵉᵗʰᵉʳ ⁱᵗ'ˢ ᵉᵈⁱᵗⁱⁿᵍ ᵈᵒᶜᵘᵐᵉⁿᵗ ᵖʳᵒᵖᵉʳᵗⁱᵉˢ, ᵃᵈᵈⁱⁿᵍ ᵗᵃᵍˢ, ᵒʳ ᵐᵃⁿᵃᵍⁱⁿᵍ ᵃᵘᵗʰᵒʳ ⁱⁿᶠᵒʳᵐᵃᵗⁱᵒⁿ, ⁱ'ᵐ ʰᵉʳᵉ ᵗᵒ ˢⁱᵐᵖˡⁱᶠʸ ᵗʰᵉ ᵖʳᵒᶜᵉˢˢ ᶠᵒʳ ʸᵒᵘ. ʲᵘˢᵗ ˢᵉⁿᵈ ᵐᵉ ᵗʰᵉ ᶠⁱˡᵉ ʸᵒᵘ ʷᵃⁿᵗ ᵗᵒ ʷᵒʳᵏ ʷⁱᵗʰ, ᵃⁿᵈ ⁱ'ˡˡ ᵍᵘⁱᵈᵉ ʸᵒᵘ ᵗʰʳᵒᵘᵍʰ ᵗʰᵉ ᵐᵉᵗᵃᵈᵃᵗᵃ ᵉᵈⁱᵗⁱⁿᵍ ᵒᵖᵗⁱᵒⁿˢ. ˡᵉᵗ'ˢ ᵍᵉᵗ ˢᵗᵃʳᵗᵉᵈ!
"""
    GROUP_START_MSG = """
Hɪ {},

ʰᵉˡˡᵒ ᵗʰᵉʳᵉ! ⁱ'ᵐ ᵗʰᵉ ᶠⁱˡᵉ ᵐᵉᵗᵃᵈᵃᵗᵃ ᵉᵈⁱᵗᵒʳ ᵇᵒᵗ, ʰᵉʳᵉ ᵗᵒ ʰᵉˡᵖ ʸᵒᵘ ᵐᵃⁿᵃᵍᵉ ᵃⁿᵈ ᵉᵈⁱᵗ ʸᵒᵘʳ ᶠⁱˡᵉ ᵐᵉᵗᵃᵈᵃᵗᵃ ᵉᶠᶠᵒʳᵗˡᵉˢˢˡʸ. ʷⁱᵗʰ ᵐʸ ᵃˢˢⁱˢᵗᵃⁿᶜᵉ, ʸᵒᵘ ᶜᵃⁿ ᵉᵃˢⁱˡʸ ᵘᵖᵈᵃᵗᵉ, ᵐᵒᵈⁱᶠʸ, ᵃⁿᵈ ᵒʳᵍᵃⁿⁱᶻᵉ ᵗʰᵉ ᵐᵉᵗᵃᵈᵃᵗᵃ ᵒᶠ ʸᵒᵘʳ ᶠⁱˡᵉˢ. ʷʰᵉᵗʰᵉʳ ⁱᵗ'ˢ ᵉᵈⁱᵗⁱⁿᵍ ᵈᵒᶜᵘᵐᵉⁿᵗ ᵖʳᵒᵖᵉʳᵗⁱᵉˢ, ᵃᵈᵈⁱⁿᵍ ᵗᵃᵍˢ, ᵒʳ ᵐᵃⁿᵃᵍⁱⁿᵍ ᵃᵘᵗʰᵒʳ ⁱⁿᶠᵒʳᵐᵃᵗⁱᵒⁿ, ⁱ'ᵐ ʰᵉʳᵉ ᵗᵒ ˢⁱᵐᵖˡⁱᶠʸ ᵗʰᵉ ᵖʳᵒᶜᵉˢˢ ᶠᵒʳ ʸᵒᵘ. ʲᵘˢᵗ ˢᵉⁿᵈ ᵐᵉ ᵗʰᵉ ᶠⁱˡᵉ ʸᵒᵘ ʷᵃⁿᵗ ᵗᵒ ʷᵒʳᵏ ʷⁱᵗʰ, ᵃⁿᵈ ⁱ'ˡˡ ᵍᵘⁱᵈᵉ ʸᵒᵘ ᵗʰʳᵒᵘᵍʰ ᵗʰᵉ ᵐᵉᵗᵃᵈᵃᵗᵃ ᵉᵈⁱᵗⁱⁿᵍ ᵒᵖᵗⁱᵒⁿˢ. ˡᵉᵗ'ˢ ᵍᵉᵗ ˢᵗᵃʳᵗᵉᵈ!

❗**Yᴏᴜ ʜᴀsɴ'ᴛ sᴛᴀʀᴛᴇᴅ ᴍᴇ ʏᴇᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ғɪʀsᴛ sᴛᴀʀᴛ ᴍᴇ sᴏ ɪ ᴄᴀɴ ᴡᴏʀᴋ ғʟᴀᴡʟᴇssʟʏ**
"""
    PROGRESS_BAR = """<b>
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

    SEND_FFMPEG_CODE = """
❪ HOW TO SET CUSTOM METADATA ❫

 ➜ <a herf=https://telegra.ph/How-To-Set-Custom-Metadata-Name-11-26>𝖱𝖾𝖺𝖽 𝖧𝖾𝗋𝖾</a>

📥 FOR HELP CONT. @Snowball_Official
"""

    
    HELP_MSG = """
Available commands:-

➜ /set_ffmpeg - To set custom ffmpeg code
➜ /set_caption - To set custom caption
➜ /del_ffmpeg - Delete the custom ffmpeg code
➜ /del_caption - Delete caption
➜ /see_ffmpeg - View custom ffmpeg code
➜ /see_caption - View caption 
➜ /cancel - To clear all ongoing process 
➜ To Set Thumbnail just send photo


<b>⦿ Developer:</b> <a href=https://t.me/Snowball_Official>ѕησωвαℓℓ ❄️</a>
"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : @{}
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/Snowball_Official>𝓢𝓝𝓞𝓦𝓑𝓐𝓛𝓛</a>
├👑 Instagram : <a href=https://www.instagram.com/ritesh6_>C-Insta</a> 
├☃️ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/+HzGpLAZXTxoyYTNl>𝖱𝖮𝖮𝖥𝖨𝖵𝖤𝖱𝖲𝖤</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├🌀 ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>
╰───────────────⍟ """
