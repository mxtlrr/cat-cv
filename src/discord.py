import requests
from datetime import datetime

file = open("../.env", "r").read().split(",")
channel_id = file[0]
token = file[1]

data = {
        "content": f"[{datetime.now()}] CAT DETECTED! <@!248252747344904192>",
        "channel": channel_id,
}
headers = {
        "Authorization": f"Bot {token}"
}

def SendToDiscord(file: str):
    r = requests.post("https://discord.com/api/v9/channels/1241443877425254463/messages",
                      data=data, headers=headers, files={"file": (file, open(file, "rb"))})
    print(r.text)