from datetime import datetime
from telethon.sync import TelegramClient
import asyncio
from termcolor import colored
from urllib.parse import urlparse, parse_qs
print("Tool by : ",colored("ANON HAWK \n","red"))

api_id = 23113647
api_hash = 'adc99cf1a956f8a58b89803dacf1d0e0'
phone = '+917003299800'

# All deep links: [(bot_username, start_param)]
link1_commands = [
    ('Airdropupdatezsbot', 'claim2003'),
    ('BuzzFollowersbot', 'claim2003'),
    ('Cusignalsbot', 'claim2003')
]

link2_commands = [
    ('Airdropupdatezsbot', '100'),
    ('BuzzFollowersbot', '150710000'),
    ('Cusignalsbot', '15000000')
]

client = TelegramClient('airdrop3', api_id, api_hash)

async def start_bots(command_list):
    for bot_username, start_param in command_list:
        try:
            await client.send_message(bot_username, f'/start {start_param}')
            print(f"Started {bot_username} with /start {start_param}")
        except Exception as e:
            print(f"Error starting {bot_username}: {e}")

async def loop_forever():
    while True:
        print("Starting all 2003 commands...")
        await start_bots(link1_commands)
        await asyncio.sleep(2)
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Sending all Link2 commands...")
        await start_bots(link2_commands)
        print("Waiting 5 minutes..Current time :",current_time,"\n")
        await asyncio.sleep(300)

with client:
    client.loop.run_until_complete(loop_forever())
