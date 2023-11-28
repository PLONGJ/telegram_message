# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import time

from requests.adapters import Retry
from telethon.sync import TelegramClient
import json
import operator

import requests

session = requests.session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
session.mount('https://', requests.adapters.HTTPAdapter(max_retries=3))


def ymgc_sign_in():
    # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzcXFfYXV0aCIsImNsaWVudFR5cGUiOjMsIm9wZW5JZCI6Im9KZ20zNU1UZXI3b0NESDFyeUoxdDIxWnlDYjAiLCJtb2JpbGUiOiIxMzUwMDI0MDkyOSIsImV4cCI6MTY5NTYzNDA0NSwiaWF0IjoxNjk1MDI5MjQ1LCJtZW1iZXJJZCI6IjExMDQ1MDEwMDA5MDk4NyJ9.9SQTob9Nu3LNAvPLx-GrOc41UR8-JiCaSvlHBXZ9SW8'

    token = os.getenv('YMGC_TOKEN')
    try:
        response = session.post('https://api.alldragon.com/mkt2/checkin/checkin.json', headers={
            "Authorization": token,
        }, params={
            "tenantId": 4142,
            "tenantCode": "zhymgc",
            "clientType": 3
        }, timeout=(15, 3))
        res = response.json()
        print("扬明广场签到：",res)
        if operator.eq(res['msg'], "SUCCESS") is not True:
            send_message_by_wx_pusher('签到失败', '扬名广场签到失败')
    except requests.exceptions.RequestException as e:
        print(e)
        send_message_by_wx_pusher('签到失败', '扬名广场签到失败')


def hfvmall_sing_in():
    try:
        # token = 'bXPCCvEodkyIl1qK-xjslQR2hgcPOJM0'
        token = os.getenv('WX_VMALL_APPID')

        response = session.post('https://m.mallcoo.cn/api/user/User/CheckinV2', {}, {
            "MallID": 12614,
            "Header": {
                "Token": '{},17403'.format(token),
                "systemInfo": {
                    "miniVersion": "DZ.2.65.0.SNS.9",
                    "system": "iOS 17.1.1",
                    "model": "iPhone 13 Pro<iPhone14,2>",
                    "SDKVersion": "3.2.2",
                    "version": "8.0.43"
                }
            }
        }, timeout=(15, 5))
        res = response.json()
        print("华发商都签到：",res)
    except requests.exceptions.RequestException as e:
        print(e)
        send_message_by_wx_pusher('签到失败', '华发商都签到失败')


def fhl_sign_in():
    try:
        # token = 'b1JzZxVARUinuC-b8DWngASFUMiLmLtU'
        token = os.getenv('WX_FHL_APPID')

        response = session.post('https://m.mallcoo.cn/api/user/User/CheckinV2', {}, {
            "MallID": 11906,
            "Header": {
                "Token": '{},16842'.format(token),
                "systemInfo": {
                    "miniVersion": "2.5.63.2",
                    "system": "iOS 16.6",
                    "model": "iPhone 13 Pro<iPhone14,2>",
                    "SDKVersion": "3.0.1",
                    "version": "8.0.40"
                }
            }
        }, timeout=(15, 5))
        res = response.json()
        print("富华里签到：",res)
    except requests.exceptions.RequestException as e:
        print(e)
        send_message_by_wx_pusher('签到失败', '富华里签到失败')


def hyc_sign_in():
    try:
        # token = 'b1JzZxVARUinuC-b8DWngASFUMiLmLtU'
        token = os.getenv('WX_HYC_APPID')

        response = session.post('https://m.mallcoo.cn/api/user/User/CheckinV2', {}, {
            "MallID": 11898,
            "Header": {
                "Token": '{},16842'.format(token),
                "systemInfo": {
                    "miniVersion": "2.5.63.2",
                    "system": "iOS 16.6",
                    "model": "iPhone 13 Pro<iPhone14,2>",
                    "SDKVersion": "3.0.1",
                    "version": "8.0.40"
                }
            }
        }, timeout=(15, 5))
        res = response.json()
        print("环宇城签到:",res)
    except requests.exceptions.RequestException as e:
        print(e)
        send_message_by_wx_pusher('签到失败', '环宇城签到失败')


def sendMessage():
    try:
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
            print('发动消息给' + to_user_name.replace('@', '') + '成功')

        client.session.save()
    except Exception as e:
        print(e)


def send_message_by_wx_pusher(summary, content):
    send_url = 'http://wxpusher.zjiecode.com/api/send/message'

    uuId = 'UID_UD4BsM92ESQcGn8JHsYeSyfkROmV'
    appToken = 'AT_gMb8L2Bp7ckyU8DO2a2dXyVc0aLB3UYS'

    headers = {
        'content-type': 'application/json'
    }

    params = {
        'appToken': appToken,
        'content': content,
        'summary': summary,
        'contentType': 1,
        'uids': [uuId]
    }
    pages = requests.post(send_url, data=json.dumps(params), headers=headers)

    result = pages.json()
    if result['code'] == 1000:
        print('发送消息成功')
    else:
        print('发送消息失败{0}'.format(result['msg']))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    ymgc_sign_in()
    hfvmall_sing_in()
    fhl_sign_in()
    hyc_sign_in()
    sendMessage()
