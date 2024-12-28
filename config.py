import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21740783")
    API_HASH  = os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7444018073:AAHIYXGx9XrkyoqM8hOn_U7UP46Vhqex7SA") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","TAF")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://boyrokey00:rajan123@cluster0.4fhuu.mongodb.net/")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/4b306f4b15c23a8f22e58.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6693549185').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002151806170"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))

    # Premium 4GB Renaming Client Config
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQGJpOEALt4IdhZRubNAl4m6iyA0sjD1NNcs1dUDtXqxTGeGCvh2bFNOhynMJuNGBUICu7rrchNnmex5X-1L1xv-f_iJb_OyISgz5NCEJPxDbPUWC-Y57qNqMaaBSmbSp0sKqRihRBwTbUuiw7RRJhWgEOpUJHjBRHcaopg-0O6DJd-TeLB2l7GyWw1ZNXUToIyDsNrd4xTUxqKPEUMGVusgU7S2k1Glc8bELlYGhvbZWus5Z5zC5ahssLLcujQfAyUpxoCdQ9d7AhOog0KdJOoMB4LMeL6AXcGF9F-MT3b4WD2W-x69zeqdzRjBPHQCVxpYgrTILAkz9nIZ4rdhS8g6TkJNowAAAAGO93SBAA")


class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

<b>Bot Is Made By :</b> @Madflix_Bots"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/Madflix_Bots>Madflix Botz</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/MadflixOfficials>Jishu Developer</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://instagram.com/jishu.editz>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/MadflixOfficials>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `madflixofficial@axl`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @Madflix_Bots</code>

💬 For Any Help Contact @MadflixOfficials
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
