from datetime import datetime
from telethon.sync import TelegramClient
import asyncio
from urllib.parse import urlparse, parse_qs
from termcolor import colored
print("Tool by : ",colored("ANON HAWK \n","red"))
api_id = 25589634
api_hash = 'cf47145c4bd1c2e24aaa363ba6786f76'
# phone = '++'  # Only needed for first login

# All deep links: [(bot_username, start_param)]
link1_commands = [
    ('Airdropupdatezsbot', 'claim2003'),
    ('Cusignalsbot', 'claim2003')
]

link2_commands = [
    ('Airdropupdatezsbot', '100'),
    ('Cusignalsbot', '15000000')
]

client = TelegramClient('airdrop_madara', api_id, api_hash)

async def start_bots(command_list):
    for bot_username, start_param in command_list:
        try:
            await client.send_message(bot_username, f'/start {start_param}')
            print(f"Started {bot_username} with /start {start_param}")
        except Exception as e:
            print(f"Error starting {bot_username}: {e}")

async def loop_forever():
    while True:
        print("Sending all Link1 commands...")
        await start_bots(link1_commands)
        await asyncio.sleep(2)
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Sending all Link2 commands...")
        await start_bots(link2_commands)
        print("Waiting 5 minutes..Current time :", current_time,"\n")
        await asyncio.sleep(300)

with client:
    client.loop.run_until_complete(loop_forever())
