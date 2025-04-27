from datetime import datetime
from telethon.sync import TelegramClient
import asyncio
from termcolor import colored
print("Tool by : ", colored("ANON HAWK\n", "red"))

# Session details for both accounts
accounts = [
    {
        'session': 'airdrop_eagle',
        'api_id': 25228452,
        'api_hash': '41a057cb918cafaa548dfd45ae0e08bb'
    }
]

# Commands
link1_commands = [
    ('BuzzFollowersbot', 'claim2003')
]

link2_commands = [
    ('BuzzFollowersbot', '15000000')
]

# Create client instances
clients = [TelegramClient(acc['session'], acc['api_id'], acc['api_hash']) for acc in accounts]

async def start_bots(client, command_list):
    for bot_username, start_param in command_list:
        try:
            await client.send_message(bot_username, f'/start {start_param}')
            print(f"[{client.session.filename}] Started {bot_username} with /start {start_param}")
        except Exception as e:
            print(f"[{client.session.filename}] Error starting {bot_username}: {e}")

async def loop_forever():
    i = 0
    while True:
        print("▶ Sending Link1 commands (claim2003)...")
        await asyncio.gather(*(start_bots(client, link1_commands) for client in clients))
        await asyncio.sleep(20)
        print("▶ Sending Link2 commands...")
        await asyncio.gather(*(start_bots(client, link2_commands) for client in clients))
        i = i + 1
        current_time = datetime.now().strftime("%H:%M:%S")
        print("⏳ Iteration : ",i," Time:", current_time, "\n")
        await asyncio.sleep(295)

async def main():
    async with clients[0]:
        await loop_forever()

asyncio.run(main())

