
from base.wms_base import get, get_token

receipt_shelf_configId = None


def get_work_config(type=0):
    url = "business/app/arrivalConfig/getWorkConfig"
    param = get_work_config_param(type)
    res = get(url, param, get_token())
    return res[0]['id']


def get_work_config_param(type):
    return {'operationType': type}


def get_receipt_shelf__config_id():
    global receipt_shelf_configId
    if receipt_shelf_configId is None:
        receipt_shelf_configId = get_work_config(0)
    return receipt_shelf_configId
