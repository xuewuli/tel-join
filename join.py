import telethon
from telethon import TelegramClient, sync
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep

from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest

import sys
import socks

if len(sys.argv) < 3:
    print("需要指定导入的源和目标群名称 \n python3 join.py source dest")
    sys.exit(2)

source_name = sys.argv[1]
dest_name = sys.argv[2]

# start client
client = TelegramClient('demo',
    11111, # 这里填 app_id
    'aaaaaaaaa', # 这里填 api_hash
    proxy=(socks.SOCKS5, 'localhost', 1086)
).start()
      
offset = 0
limit = 100

source_info = client.get_entity(source_name)
if type(source_info) is telethon.tl.types.Channel:
    dest_info = client.get_entity(dest_name)
    if type(dest_info) is telethon.tl.types.Channel:
        while True:
            participants = client(GetParticipantsRequest(
                source_info.id, ChannelParticipantsSearch(''), offset, limit, hash=0
            ))
            if not participants.users:
                break
            offset += len(participants.users)
            for user in participants.users:
                if user.username is not None:
                    print(user.username)
                    try:
                        client(InviteToChannelRequest(dest_info.id, [user.username]))
                    except:
                        print('邀请失败')
                    sleep(1) #防止被服务器bind
    else:
        print(dest_name,"不是一个频道")
else:
    print(source_name,"不是一个频道")

