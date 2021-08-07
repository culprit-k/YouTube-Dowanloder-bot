from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("👥 𝐆𝐑𝐎𝐔𝐏 - 𝟏", url="https://t.me/Movie_House_1"),
        [InlineKeyboardButton(
            "𝐆𝐑𝐎𝐔𝐏 - 𝟐 👥", url="https://t.me/Movie_House_Group_2")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

    
    
   
