from telethon.sync import TelegramClient
import asyncio

api_id = 25228452
api_hash = '41a057cb918cafaa548dfd45ae0e08bb'
bot_username = 'Free_Binance_Bnb_Pay_Bot'

client = TelegramClient('airdrop_eagle', api_id, api_hash)

async def mine_bnb():
    await client.start()
    while True:
        try:
            print("Sending Free Bnb Collect command...")
            await client.send_message(bot_username, "✅ Free Bnb Collect 🎰")
            await asyncio.sleep(5)  # Wait for the bot's response

            messages = await client.get_messages(bot_username, limit=5)
            for msg in messages:
                if msg.buttons:
                    for i, row in enumerate(msg.buttons):
                        for j, button in enumerate(row):
                            if "🔮 Collect Treasure" in button.text:
                                print("Clicking Collect Treasure button...")
                                await msg.click(i, j)
                                break
            await asyncio.sleep(65)  # Delay to avoid overlapping
        except Exception as e:
            print("Error:", e)
            await asyncio.sleep(70)  # Extra delay on error

with client:
    client.loop.run_until_complete(mine_bnb())
