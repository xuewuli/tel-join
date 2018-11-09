# 拉人工具

把A群的用户自动邀请到B群

### 限制
* 必须见过这个用户（即运行工具的用户要先加入A群）
* 用户设置了username
* 用户隐私设置没有开启拒绝邀请

#### 获得appid和hash
    需要在 https://my.telegram.org/ 用手机号注册
获得后修改`join.py`中`TelegramClient`创建的参数
`TelegramClient`创建时可以指定代理


#### 登陆
    首次启动会在要求输入手机号，获取验证码登陆，然后会生*.session文件，重复运行不需要再登陆
    所有邀请均由登陆用户执行

#### 登陆
#### 运行环境 
    python3
#### 依赖库
    pip3 install PySocks telethon

#### 运行方式
    python3 join.py chanel_source chanel_dest