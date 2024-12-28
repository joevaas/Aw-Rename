
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import jishubotz
from config import Config, Txt  
  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await jishubotz.add_user(client, message)                
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton('🔊 Updates', url='https://t.me/Madflix_Bots'),
        InlineKeyboardButton('♻️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/MadflixBots_Support')],
        [InlineKeyboardButton('❤️‍🩹 About', callback_data='about'),
        InlineKeyboardButton('🛠️ Help', callback_data='help')],
        [InlineKeyboardButton("👨‍💻 Developer", url='https://t.me/CallAdminRobot')]
    ])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton('🔊 Updates', url='https://t.me/Madflix_Bots'),
                InlineKeyboardButton('♻️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/MadflixBots_Support')],
                [InlineKeyboardButton('❤️‍🩹 About', callback_data='about'),
                InlineKeyboardButton('🛠️ Help', callback_data='help')],
                [InlineKeyboardButton("👨‍💻 Developer", url='https://t.me/CallAdminRobot')]
            ])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⚡ 4GB Rename Bot", url="https://t.me/FileRenameXProBot")],
                [InlineKeyboardButton("🔒 Close", callback_data = "close"),
                InlineKeyboardButton("◀️ Back", callback_data = "start")]
            ])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🤖 More Bots", url="https://t.me/Madflix_Bots/7")],
                [InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")]
            ])            
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    user_id = message.chat.id
    old = insert(int(user_id))
        
    user_id = message.from_user.id    
    if FORCE_SUBS:
        try:
            await client.get_chat_member(FORCE_SUBS, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("<b>Hello Dear \n\nYou Need To Join In My Channel To Use Me\n\nKindly Please Join Channel</b>",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup([
                                         [InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{FORCE_SUBS}")]
                                         ]))
            await client.send_message(LOG_CHANNEL, f"<b><u>New User Started The Bot</u></b> \n\n<b>User ID :</b> <code>{user_id}</code> \n<b>First Name :</b> {message.from_user.first_name} \n<b>Last Name :</b> {message.from_user.last_name} \n<b>User Name :</b> @{message.from_user.username} \n<b>User Mention :</b> {message.from_user.mention} \n<b>User Link :</b> <a href='tg://openmessage?user_id={user_id}'>Click Here</a> \n<b>User Plan :</b> {user}")
            return
		
    botdata(int(botid))
    bot_data = find_one(int(botid))
    prrename = bot_data['total_rename']
    prsize = bot_data['total_size']
    user_deta = find_one(user_id)
    used_date = user_deta["date"]
    buy_date = user_deta["prexdate"]
    daily = user_deta["daily"]
    user_type = user_deta["usertype"]

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 120
    else:
        LIMIT = 10
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"<b>Sorry Dude I Am Not Only For You \n\nFlood Control Is Active So Please Wait For {ltime} </b>", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        file_id = file.file_id
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% Of Daily {humanbytes(limit)} Data Quota Exhausted.\n\n<b>File Size Detected :</b> {humanbytes(file.file_size)}\n<b>Used Daily Limit :</b> {humanbytes(used)}\n\nYou Have Only <b>{humanbytes(remain)}</b> Left On Your Account.\n\nIf U Want To Rename Large File Upgrade Your Plan", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Upgrade", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING_SESSION:
                if buy_date == None:
                    await message.reply_text(f"You Can't Upload More Than 2GB File.\n\nYour Plan Doesn't Allow To Upload Files That Are Larger Than 2GB.\n\nUpgrade Your Plan To Rename Files Larger Than 2GB.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Upgrade", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__What Do You Want Me To Do With This File ?__\n\n**File Name :** `{filename}`\n**File Size :** {humanize.naturalsize(file.file_size)}\n**DC ID :** {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rename", callback_data="rename"), InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Your Plan Expired On {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("You Can't Upload More Than 2GB File.\n\nYour Plan Doesn't Allow To Upload Files That Are Larger Than 2GB.\n\nUpgrade Your Plan To Rename Files Larger Than 2GB.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Upgrade", callback_data="upgrade")]]))
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")
            
            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__What Do You Want Me To Do With This File ?__\n\n**File Name :** `{filename}`\n**File Size :** {filesize}\n**DC ID :** {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rename", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))



@Client.on_message(filters.private & filters.command(["donate", "d"]))
async def donate(client, message):
	text = Txt.DONATE_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("🦋 Admin",url = "https://t.me/CallAdminRobot"), 
        			InlineKeyboardButton("✖️ Close",callback_data = "close") ]])
	await message.reply_text(text = text,reply_markup = keybord)



# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
