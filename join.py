import telethon
from telethon import TelegramClient, sync
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.functions.channels import InviteToChannelRequest
import socks
import random

# 对方的群组
source_name = "Cyasmr"
# 自己的群组
dest_name = "taotujingxuan"

proxy = (socks.SOCKS5, "127.0.0.1", 1080)
# start client
api_id = 1234567
api_hash = "xxxxxxxxx"
client = TelegramClient('anon', api_id, api_hash, proxy=proxy).start()

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
            num = 0
            for user in participants.users:
                if user.username is not None:
                    print(user.username + ": ", end="")
                    try:
                        client(InviteToChannelRequest(dest_info.id, [user.username]))
                    except telethon.errors.rpcerrorlist.PeerFloodError:
                        print("请求过多")
                    except telethon.errors.rpcerrorlist.UserPrivacyRestrictedError:
                        print("对方设置了隐私或者无用户名")
                    except telethon.errors.rpcerrorlist.UserNotMutualContactError:
                        print("无法获取账户的相关信息")
                    except telethon.errors.rpcerrorlist.FloodWaitError as e:
                        exit("被TG限制暂时无法使用,需要等待: {}小时".format(int(str(e).split(" ")[3]) // 60 // 60))
                    except telethon.errors.rpcerrorlist.UserBotError:
                        print("机器人，跳过")
                    else:
                        num += 1
                        print("邀请成功,{}人".format(num))
                    # 随机秒数
                    x = lambda: int(random.randint(1, 10))
                    sleep(x())  # 防止被服务器bind
    else:
        print(dest_name, "不是一个频道")
else:
    print(source_name, "不是一个频道")
