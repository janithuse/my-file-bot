import os
from pyrogram import Client, filters

# ඔයා ලබාදුන් නිවැරදි විස්තර
API_ID = 27095170
API_HASH = "d61d324f1c991f9ce3a5e0eb94301e5f"
BOT_TOKEN = "8645273337:AAFDagl9S8_XDOh9HGWt8b4AUFOfyxNjK84"
# Channel ID එකේ මුලට -100 එකතු කර ඇත
CHANNEL_ID = -1003874244140 

app = Client(
    "my_file_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    # Deep Linking පරීක්ෂාව (උදා: t.me/bot?start=v_123)
    if len(message.command) > 1:
        data = message.command[1]
        if data.startswith("v_"):
            try:
                # v_ කෑල්ල ඉවත් කර Message ID එක ලබා ගැනීම
                msg_id = int(data.replace("v_", ""))
                
                # වීඩියෝව චැනල් එකෙන් කොපි කර යූසර්ට එවයි
                await client.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=CHANNEL_ID,
                    message_id=msg_id
                )
            except Exception as e:
                await message.reply("❌ කණගාටුයි, එම වීඩියෝව සොයාගත නොහැක. පසුව උත්සාහ කරන්න.")
    else:
        # සාමාන්‍යයෙන් බොට්ව ස්ටාර්ට් කරන අයට යන මැසේජ් එක
        await message.reply(
            "👋 **ආයුබෝවන්!**\n\nමම හරහා වීඩියෝ ලබා ගැනීමට ඔබගේ බ්ලොග් අඩවියේ ඇති ලින්ක් එක භාවිතා කරන්න."
        )

print("✅ බොට් සාර්ථකව වැඩ ආරම්භ කළා...")
app.run()
