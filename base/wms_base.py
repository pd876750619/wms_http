import json

import requests

from base.receipt_config import get_environment as base_environment

token = ""


def get_token():
    if token is None or token == "":
        return get_token_by_login()
    else:
        return token


def get_token_by_login():
    global token
    res = login()
    token = res['token']
    return token


def login():
    url = "login"
    data = {"username": "pengdi2", "password": "123456"}
    return post(url, data)


def get_header(user_token, url):
    head = {}
    if user_token is None and 'login' in url:
        pass
    else:
        user_token = get_token()
        head = {'token': user_token}
    return head


def post(url, data, user_token=None):
    url = get_environment() + url
    data = json.dumps(data)
    head = get_header(user_token, url)
    head['Content-Type'] = 'application/json'
    res = requests.post(url, data, headers=head)

    return get_result_data(res)


def get(url, param, user_token=None):
    url = get_environment() + url
    head = get_header(user_token, url)
    res = requests.get(url, param, headers=head)
    return get_result_data(res)


def put(url, data, user_token=None):
    url = get_environment() + url
    data = json.dumps(data)
    head = get_header(user_token, url)
    head['Content-Type'] = 'application/json'
    res = requests.put(url, data, headers=head)


def kafka_put(topic, value):
    url = "api/message"
    data = {'topic': topic, 'value': value}
    post(url, data)


def get_result_data(res):
    if res.text is not None and res.text != '':
        text = json.loads(res.text)
        print('post结果:', text)
    else:
        return
    if text['code'] != 0:
        print("调用接口失败,url:", res.url, ",msg:", text)
    else:
        return text['data']


def switch_warehouse(warehouse_code):
    url = "business/warehouse/switch"
    param = {"warehouseCode": warehouse_code}
    put(url, param)


def get_environment():
    return base_environment()
