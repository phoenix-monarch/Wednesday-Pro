class script(object):
    START_TXT = """<b>ʜᴇʟʟᴏ {},
ᴍʏ ɴᴀᴍᴇ ɪs <a href=https://t.me/{}>{}</a>, ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴɪᴍᴇ ᴡᴇʙsᴇʀɪᴇs , ɪᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴɪᴏʏ</b>"""
    
    HELP_TXT = """<b>ʜᴇʏ {}
ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.
ᴄʟɪᴄᴋ /more ᴛᴏ ꜱᴇᴇ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇ ᴄᴏᴍᴍᴀɴᴅꜱ.</b>"""


# ⚠️ Please don't change our credits 𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾 & 𝙳𝙴𝚅 👇🏻

    ABOUT_TXT = """<b>× ᴍʏ ɴᴀᴍᴇ :  {}
× ᴍʏ ᴄʀᴇᴀᴛᴏʀ: <a href='https://t.me/xenxd'>ᴍɪᴋєʏ ꜱᴀɴσ</a>
× ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
× ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 𝟹</a>
× ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴀɴɢᴏ ᴅʙ</a>
× ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://app.koyeb.com/'>ᴋᴏʏᴇʙ</a>
× ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ: v2.0.1 [  ʙᴇᴛᴀ]</b>

× ᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href='https://t.me/team_netflix'>ᴛᴇᴀᴍ ɴᴇᴛғʟɪx | ᴏʀɪɢɪɴᴀʟꜱ</a></b>"""



    SOURCE_TXT = """<b>ɴᴏᴛᴇ:</b>
× ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɴᴏᴛ ᴀɴ  ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ ⚠️.
× ꜱᴏᴜʀᴄᴇ - <a href="https://t.me/xenxd">ʜᴇʀᴇ</a>

× ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴏᴜʀ ᴀʟʟ ᴄʜᴀɴɴᴇʟꜱ - @Team_Netflix
× Dᴇᴠᴇʟᴏᴘᴇʀ - <a href="https://t.me/xenxd">ᴍɪᴋєʏ ꜱᴀɴσ</a></b>"""

    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>ɴᴏᴛᴇ:</b>

<b>ɴᴏᴛᴇ:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇꜱ:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>

- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/team_netflix)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>

<b>ɴᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇx</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ.
4.ᴜꜱᴇ /set_template ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴩʟᴀᴛᴇ ꜰᴏʀ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Elsa

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    SONG_TXT = """<b>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴</b>

<i>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝙴 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚂𝙾𝙽𝙶 𝚆𝙸𝚃𝙷 𝚂𝚄𝙿𝙴𝚁 𝙵𝙰𝚂𝚃 𝚂𝙿𝙴𝙴𝙳.𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂../</i>

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂</b>

⏭️ /song 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 

<b>𝚆𝙾𝚁𝙺𝚂 𝙱𝙾𝚃𝙷 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙿𝙼</b>
@𝙲𝙸𝙽𝙴𝙼𝙰𝙻𝙰.𝙲𝙾𝙼"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.
• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦
𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/example...)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/example...</code>
<code>/video https://youtu.be/example...</code>"""

    TTS_TXT = """Help: <b> TTS 🎤 module:</b>
Translate text to speech
<b>Commands and Usage:</b>
• /tts <text> : convert text to speech"""

    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋
𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾
➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
✒️ /telegraph - Send me Picture or Vide Under (5MB)
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽
𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>

⚠️ This service has been stopped"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    DEPLOY_TXT= """𝙸𝙵 𝚈𝙾𝚄 𝙵𝙰𝙲𝙸𝙽𝙶 𝙰𝙽𝚈 𝙸𝚂𝚂𝚄𝙴 𝙸𝙽 𝚃𝙷𝙴 𝚁𝙴𝙿𝙾 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴..."""
   
    PINGS_TXT = """<b>Ping Testing:</b>
Helps you to know your ping 🚶🏼‍♂️
<b>Commands:</b>
• /alive - To check you are alive.
• /help - To get help.

• /ping - <b>To get your ping.</b>

<b>🛠️Usage🛠️ :</b>
• This commands can be used in pm and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
 
    STICKER_TXT = """<b>𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.</b>
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]"""

    FONT_TXT= """⚙️ 𝐔𝐒𝐀𝐆𝐄

𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐌𝐎𝐃𝐔𝐋𝐄 𝐓𝐎 𝐂𝐇𝐀𝐍𝐆𝐄 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄 

<b>COMMAND</b> : /font your text (optional)
        <b> Eg:- /font Hello</b>

 <i>This feature added by @team_netflix"""
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json or /js
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
<b>Everyone can use this command , if spaming happens bot will automatically ban you from the group.</b>"""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- <b>Give a user details</b>

•/whois :-give a user full details 📑"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>"""

    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>⚡ 𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙺𝙸𝙽𝙳 𝙾𝙵 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶'𝚂 ⚡</b>
 
𝟣. /dice - 𝚁𝙾𝙻𝙴 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴 
𝟤. /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝙰𝚁𝚃 
3. /Runs - 𝚂𝙾𝙼𝙴 𝚁𝙰𝙽𝙳𝙾𝙼 𝙳𝙸𝙰𝙻𝙾𝙶𝚄𝙴𝚂 
4. /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
5. /luck or /cownd - 𝚂𝙿𝙸𝙽 𝙰𝙽𝙳 𝚃𝚁𝚈 𝚈𝙾𝚄𝚁 𝙻𝚄𝙲𝙺"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a message to all groups</code>
• /gfilter - <code>To add global filter</code>
• /gfilters - <code>To view global filters</code>
• /delallg - <code>To delete all global filters from database</code>
• /delg - <code>To delete a specific global filter</code>
• /setskip - <code>Skip no of files before indexing</code>
• /send - <code>Send any message through bot to users. /send (username/userid) reply with message </code>
• /deletefiles - <code>Delete CamRip and PreDvD files delete from database </code>"""
    
    STATUS_TXT = """<b>× ᴛᴏᴛᴀʟ ғɪʟᴇs - <code>{}</code>
× ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
× ᴛᴏᴛᴀʟ ᴄʜᴀᴛs - <code>{}</code>
× ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{}</code>
× ғʀᴇᴇ sᴛᴏʀᴀɢᴇ - <code>{}</code></b>"""

    CARB_TXT = """<b>Help</b> : 𝗖𝗔𝗥𝗕𝗢𝗡
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""


    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
wednesday
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
wednesday
"""
    FILE_MSG = """
<b>Hai 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 Fɪʟᴇ Nᴀᴍᴇ</b> : <code>{}</code>              
                       
<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{}</b>
"""
    CHANNEL_CAP = """
<b>Hai 👋 {}</b> 😍

<code>{}</code>

⚠️ <b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>

<b>Due to copyright the file will be deleted from here in 10 minutes so download after moving from here to somewhere else!</b>

<b>© Powered by {}</b>
"""
    SUR_TXT = """
<b>
 ʜᴇʟʟᴏ{},
ᴍʏ ɴᴀᴍᴇ ɪs <a href=https://t.me/{}>{}</a>, ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴɪᴍᴇ ᴡᴇʙsᴇʀɪᴇs , ɪᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴɪᴏʏ</b>
</b>
"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

× ᴛɪᴛᴛʟᴇ: <a href={url}>{title}</a>
× ɢᴇɴʀᴇ: {genres}
× ʀᴇʟᴇᴀsᴇ: <a href={url}/releaseinfo>{year}</a>
× ʀᴀᴛɪɴɢ: <a href={url}/ratings>{rating}</a> / 10
× ʀᴇǫᴜᴇꜱᴛᴇᴅ ʙʏ: {message.from_user.mention}

× ɴᴏᴛᴇ: ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ ᴀ ғᴇᴡ ᴍɪɴᴜᴛᴇꜱ ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ

©ᴡɪᴢᴀʀᴅ ɴᴇᴛᴡᴏʀᴋ</b>"""

    CUSTOM_FILE_CAPTION = """<b>📂Fɪʟᴇɴᴀᴍᴇ : {file_name}

╭─────── • ◆ • ───────╮
🔅 ᴘᴏᴡᴇʀᴇᴅ ʙʏ :  <a href="https://t.me/+QNl7gpHtzL8xYTc1">ᴋᴀɪᴢᴏʏᴜ ɴᴇᴛᴡᴏʀᴋ</a>
╰─────── • ◆ • ───────╯

╭─────── • ◆ • ───────╮
▫️ ᴄʜᴀɴɴᴇʟ : @team_netflix
▫️ main channel : @netflix_complex
╰─────── • ◆ • ───────╯</b>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} , Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ"""

    ALRT_TXT = """ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏʏ ꜱɪʀ"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧 """

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""

    MVE_NT_FND = """<b>ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɪꜱ ɴᴏᴛ ʏᴇᴛ  ʀᴇʟᴇᴀꜱᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ</b> """

    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    I_CUDNT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇꜱ ɪɴ ᴛʜᴀᴛ ɴᴀᴍᴇ. 
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 

╭─────── • ◆ • ───────╮
➠ ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ 
➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ 
➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ
➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ 
╰─────── • ◆ • ───────╯

ᴇxᴀᴍᴘʟᴇ : ᴋᴀɴᴛᴀʀᴀ 2022 
🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ' : ( ! , . / )"""

    I_CUD_NT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴘᴇʟʟɪɴɢ."""
    
    CUDNT_FND = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    REPRT_MSG = """ Reported To Admin"""

    CON_TXT = """<b><u>ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ</b></u>
<b>Tʜɪs ᴍᴏᴅᴜʟᴇ ɪs ᴛᴏ ғɪɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴜɴᴛʀɪᴇs</b>
• /country [𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾] 
𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :- <code>/country India</code>"""
