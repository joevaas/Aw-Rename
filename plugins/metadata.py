from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from helper.database import jishubotz
from pyromod.exceptions import ListenerTimeout
from config import Txt
import os
import asyncio 
import time
from concurrent.futures import ThreadPoolExecutor
from pyrogram.errors import MessageNotModified
from plugins.file_rename import rename_start
from plugins.auto_code import auto_rename_files



ON = [[InlineKeyboardButton('Metadata On ✅', callback_data='metadata_1')], [
    InlineKeyboardButton('Set Custom Metadata', callback_data='cutom_metadata')]]
OFF = [[InlineKeyboardButton('Metadata Off ❌', callback_data='metadata_0')], [
    InlineKeyboardButton('Set Custom Metadata', callback_data='cutom_metadata')]]

user_modes ={}

@Client.on_message(filters.command("mode"))
async def select_mode(client, message):
    user_id = message.from_user.id
    current_mode = user_modes.get(user_id, "Normal rename")
    
    # Create buttons with the current mode indicated by ✅
    remove_audio_button = InlineKeyboardButton(
        f"Normal Rename {'✅' if current_mode == 'Normal rename' else ''}", 
        callback_data="Normal_rename"
    )
    trim_video_button = InlineKeyboardButton(
        f"Auto Rename {'✅' if current_mode == 'Auto rename' else ''}", 
        callback_data="Auto_rename"
    )
    Cancel = InlineKeyboardButton("❌ Close", callback_data="close")
    await message.reply(
        "Choose an Rename mode to perform task👇☘️:",
        reply_markup=InlineKeyboardMarkup([[remove_audio_button, trim_video_button], [Cancel]])
  )


@Client.on_message(filters.video | filters.document | filters.audio & filters.incoming)
async def handle_video(client, message: Message):
    user_id = message.from_user.id
    current_mode = user_modes.get(user_id, "Normal rename")
    
    # Process based on current mode
    if current_mode == "Normal rename":
        await rename_start(client, message)
    elif current_mode == "Auto rename":
        await auto_rename_files(client, message)
@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):

    ms = await message.reply_text("**Please Wait...**", reply_to_message_id=message.id)
    bool_metadata = await jishubotz.get_metadata(message.from_user.id)
    user_metadata = await jishubotz.get_metadata_code(message.from_user.id)
    await ms.delete()
    if bool_metadata:
        return await message.reply_text(f"**Your Current Metadata :-**\n\n➜ `{user_metadata}` ",quote=True, reply_markup=InlineKeyboardMarkup(ON))
    return await message.reply_text(f"**Your Current Metadata :-**\n\n➜ `{user_metadata}` ",quote=True, reply_markup=InlineKeyboardMarkup(OFF))


@Client.on_callback_query(filters.regex('.*?(custom_metadata|metadata|Auto_rename|Normal_rename).*?'))
async def query_metadata(bot: Client, query: CallbackQuery):
    user_id = query.from_user.id
    data = query.data

    if data in ["Normal_rename", "Auto_rename"]:
        if data == "Normal_rename":
            user_modes[user_id] = "Normal rename"
        elif data == "Auto_rename":
            user_modes[user_id] = "Auto rename"

        # Update buttons based on selected mode
        remove_audio_button = InlineKeyboardButton(
            f"Normal Rename {'✅' if user_modes[user_id] == 'Normal rename' else ''}", 
            callback_data="Normal_rename"
        )
        trim_video_button = InlineKeyboardButton(
            f"Auto Rename {'✅' if user_modes[user_id] == 'Auto rename' else ''}", 
            callback_data="Auto_rename"
        )
       
        Cancel = InlineKeyboardButton("❌ Close", callback_data="close")
        
        new_markup = InlineKeyboardMarkup([[remove_audio_button, trim_video_button], [Cancel]])
        await query.message.edit_reply_markup(reply_markup=new_markup)
        await query.answer("Mode selected ✅.")
        
    elif data.startswith('metadata_'):
        _bool = data.split('_')[1]
        user_metadata = await jishubotz.get_metadata_code(query.from_user.id)

        if bool(eval(_bool)):
            await jishubotz.set_metadata(query.from_user.id, bool_meta=False)
            await query.message.edit(f"**Your Current Metadata :-**\n\n➜ `{user_metadata}` ", reply_markup=InlineKeyboardMarkup(OFF))

        else:
            await jishubotz.set_metadata(query.from_user.id, bool_meta=True)
            await query.message.edit(f"**Your Current Metadata :-**\n\n➜ `{user_metadata}` ", reply_markup=InlineKeyboardMarkup(ON))

    elif data == 'cutom_metadata':
        await query.message.delete()
        try:
            try:
                metadata = await bot.ask(text=Txt.SEND_METADATA, chat_id=query.from_user.id, filters=filters.text, timeout=30, disable_web_page_preview=True, reply_to_message_id=query.message.id)
            except ListenerTimeout:
                await query.message.reply_text("⚠️ Error !!\n\n**Request Timed Out.**\n\nRestart By Using /metadata", reply_to_message_id=query.message.id)
                return
            print(metadata.text)
            ms = await query.message.reply_text("**Please Wait...**", reply_to_message_id=metadata.id)
            await jishubotz.set_metadata_code(query.from_user.id, metadata_code=metadata.text)
            await ms.edit("**Your Metadata Code Set Successfully ✅**")
        except Exception as e:
            print(e)
