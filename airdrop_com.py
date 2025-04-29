from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import StartBotRequest
import time
from termcolor import colored

print ("Tool by : ", colored("ANON HAWK\n", "red"))

# Session details for both accounts
accounts = [
    {
        'session': 'airdrop_arijit',
        'api_id': 24011027,
        'api_hash': '241df703a254774788c6965b04feff9c'
    },
    {
        'session': 'airdrop2',
        'api_id': 25228452,
        'api_hash': '41a057cb918cafaa548dfd45ae0e08bb'
    },
    {
        'session': 'airdrop3',
        'api_id': 23113647,
        'api_hash': 'adc99cf1a956f8a58b89803dacf1d0e0'
    },
    {
        'session': 'airdrop_oreo',
        'api_id': 24276540,
        'api_hash': '91baf3131ba2335868760f960d7f15eb'
    }
]

# Commands
link1_commands = [
    ('Airdropupdatezsbot', 'claim2003'),
#    ('BuzzFollowersbot', 'claim2003'),
    ('Cusignalsbot', 'claim2003')
]

link2_commands = [
    ('Airdropupdatezsbot', '100'),
#    ('BuzzFollowersbot', '15000000'),
    ('Cusignalsbot', '15000000')
]

def start_bots(client, command_list):
    for bot_username, start_param in command_list:
        try:
            client.send_message(bot_username, '/start ' + start_param)
            print ("[{}] Started {} with /start {}".format(client.session.filename, bot_username, start_param))
        except Exception as e:
            print ("[{}] Error starting {}: {}".format(client.session.filename, bot_username, str(e)))

def main_loop():
    clients = []
    for acc in accounts:
        client = TelegramClient(acc['session'], acc['api_id'], acc['api_hash'])
        client.start()
        clients.append(client)

    i = 0
    while True:
        print ("▶ Sending Link1 commands (claim2003)...")
        for client in clients:
            start_bots(client, link1_commands)
        time.sleep(20)

        print ("▶ Sending Link2 commands...")
        for client in clients:
            start_bots(client, link2_commands)

        current_time = datetime.now().strftime("%H:%M:%S")
        i += 1
        print ("⏳ Iteration : ", i, " Time:", current_time, "\n")
        time.sleep(295)

if __name__ == "__main__":
    main_loop()
