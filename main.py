# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import time
from telethon.sync import TelegramClient

import requests

def get_JF():
    jf_url = 'https://wx.huafamall.cn/wxmall/wxsite/mbr/signin.do?wxpubid=gh_3e33c7377a96&wxopenid=oLVyYjuadRRvvzJ21X7JAYQDED_o'
    response = requests.get('https://wx.huafamall.cn/wxmall/wxsite/mbr/signin.do',{
        'wxpubid':'gh_3e33c7377a96',
        'wxopenid':'oLVyYjuadRRvvzJ21X7JAYQDED_o'
    })
    res = response.json()
    print(res['message'])

def sendMessage():

    api_id = os.getenv('TG_APP_ID')

    api_hash = os.getenv('TG_APP_HASH')

    to_user_name_arr = os.getenv('TG_TO_USER_NAME').split(',')

    message_content = os.getenv('TG_MESSAGE_CONTENT')

    session_name = 'PLONGJ_CheckIn'

    client = TelegramClient(session_name, api_id, api_hash)
    client.start()

    for to_user_name in to_user_name_arr:
        client.send_message(to_user_name, message_content)
        time.sleep(5)
        client.send_read_acknowledge(to_user_name)
        print('发动消息给'+to_user_name.replace('@','')+'成功')
    
    client.session.save()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    sendMessage()
    get_JF()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
