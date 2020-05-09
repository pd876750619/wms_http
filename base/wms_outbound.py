import time

from base.receipt_config import get_warehouse_code, get_wave_template_id, get_outbound_num
from base.wms_base import kafka_put, get, post
from base.wms_item import get_item_1, get_item_2


def do_outbound_wave():
    outbound_num = get_outbound_num()
    for i in range(outbound_num):
        outbound_notice_put()
    time.sleep(outbound_num)
    create_and_run_wave()


def get_wave_param():
    return {
        "ids": [
            get_wave_template_id()
        ]
    }


def create_and_run_wave():
    url = "business/wave/nav/createAndRun"
    param = get_wave_param()
    res = post(url, param)
    print("创建并运行波次结果:", res)
    return res


def outbound_notice_put():
    topic = "WMS_OUTBOUND_NOTICE_CREATE"
    data = get_value()
    return kafka_put(topic, data)


def get_express():
    return {
        "toCity": "佛山",
        "toWarehouse": "广州",
        "transLineName": "广州-佛山",
        "transLineType": 1,
        "shippingMethod": 1,
        "ferryClass": "",
        "fromCity": "广州",
        "fromWarehouse": "广州",
        "deliveryPerson": "配送商1",
        "deliveryPersonPhone": "13899998888",
        "destinationCode": "F4-佛山",
        "distributionPoint": "佛山收货点",
        "expressNo": "",
        "expressType": 0,
        "needInspection": True,
        "needUrgent": False,
    }


def get_value():
    detail1 = fill_detail(get_item_1())
    detail2 = fill_detail(get_item_2())
    time_str = time.time().__str__().replace(".", "")
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    order_no = 'O999' + time_str
    return {
        "carrierName": "承运商",
        "className": "晚班",
        "departDate": localtime,
        "outboundType": 1,
        "payDate": "2020-03-10 15:00:00",
        "payType": 1,
        "countryName": "中国",
        "provinceName": "广东",
        "cityName": "佛山",
        "countyName": "禅城",
        "townName": "xx街道",
        "recipientsAddress": "测试地址",
        "recipientsName": "收货人",
        "recipientsPhone": "18999996666",
        "clientName": "客户1",
        "remark": "无",
        "sourceNo": order_no,
        "sourcePlatform": "ERP",
        "sourceType": 1,
        "vip": False,
        "warehouseCode": get_warehouse_code(),
        "ownerCode": "1003399",
        "details": [
            detail1,
            detail2
        ],
        "express": get_express()
    }


def fill_detail(item):
    detail_no = time.time().__str__().replace(".", "")
    detail = item
    detail["qualityStatus"] = 1
    detail["salePrice"] = 1000
    detail["lotNumber"] = "批号1"
    detail["costPrice"] = 800
    detail["packType"] = 2
    detail["scheduledQuantity"] = 2
    detail["sourceDetailNo"] = detail_no
    return detail
