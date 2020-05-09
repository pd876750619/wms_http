import time

import base
from base.receipt_config import get_arrival_notice_code, get_location_code, get_warehouse_code, get_need_put_arrival
from base.wms_arrival_notice import arrival_notice_put
from base.wms_base import post, kafka_put, get, switch_warehouse
from base.wms_item import get_item_1
from base.wms_work_config import get_receipt_shelf__config_id

arrival_notice_code = None


def get_wait_receipt():
    url = "app/receipt/getWaitReceive"
    param = get_wait_receipt_param()
    return get(url, param)


def get_wait_receipt_param():
    item1 = get_item_1()
    config_id = get_receipt_shelf__config_id()
    return {
        'itemCode': item1['itemCode'],
        'configId': config_id
    }


def get_wait_receipt_code():
    wait_receive_arrival_list = get_wait_receipt()
    if wait_receive_arrival_list is not None and len(wait_receive_arrival_list):
        global arrival_notice_code
        arrival_notice_code = wait_receive_arrival_list[0]['arrivalNoticeCode']
        return arrival_notice_code
    else:
        raise Exception("待收货列表为空")


def get_wait_receipt_detail_param():
    config_id = get_receipt_shelf__config_id()
    # 优先使用全局配置
    now_arrival_notice_code = get_arrival_notice_code()
    if get_arrival_notice_code() is None:
        now_arrival_notice_code = get_wait_receipt_code()
        if now_arrival_notice_code is None:
            raise Exception("待收货到货通知单号为空")
    global arrival_notice_code
    arrival_notice_code = now_arrival_notice_code
    return {
        'arrivalNoticeCode': now_arrival_notice_code,
        'configId': config_id
    }


def get_wait_receipt_detail():
    url = "app/receipt/getWaitReceiveDetail"
    param = get_wait_receipt_detail_param()
    res = get(url, param)
    return res


def receipt_shelf_inventory():
    url = "app/receipt/receiptShelfInventory"
    param_list = get_receipt_shelf_param_list()
    if len(param_list):
        for param in param_list:
            res = post(url, param)


# 组装收货上架参数
def get_receipt_shelf_param_list():
    wait_receipt_details = get_wait_receipt_detail()
    config_id = get_receipt_shelf__config_id()
    param_list = []
    if wait_receipt_details is None or len(wait_receipt_details) <= 0:
        return param_list
    for i, wait_receipt_detail in enumerate(wait_receipt_details):
        quantity = wait_receipt_detail['uncollectedQuantity']
        arrival_notice_detail_id = wait_receipt_detail['id']
        j = 0
        # 每次收货十个，批号不同，库位相同
        while j <= quantity // 10:
            param = {
                "configId": config_id,
                "goodsQuality": 1,
                "receivedQuantity": quantity - j * 10 if j == quantity // 10 else 10,
                "locationCode": get_location_code(),
                "lotNumber": i.__str__() + j.__str__(),
                "arrivalNoticeDetailId": arrival_notice_detail_id,
                "arrivalNoticeCode": arrival_notice_code
            }
            param_list.append(param)
            j = j + 1
    return param_list


def do_receive_shelf():
    if get_need_put_arrival():
        arrival_notice_put()
        time.sleep(1)
    switch_warehouse(get_warehouse_code())
    receipt_shelf_inventory()
