import base
from base.receipt_config import get_warehouse_code
from base.wms_base import post


def item_put():
    url = "api/item/put"
    data = get_data()

    return post(url, data)


def get_data():
    return {
        "itemPutDTOS": [
            get_item_1()
            ,
            get_item_2()
            ,
            get_item_3()
        ],
        "messageId": 100001586334581660
    }


def get_item_1():
    return {
        "brand": " 宝马 丰田 雷克萨斯",
        "fragileGoods": 0,
        "itemCode": "153494",
        "itemName": "大灯13246",
        "modifiedPartsName": "燃油滤清器",
        "ownerCode": "1003399",
        "ownerItemCode": "23300-0D060",
        "partsBrand": "www",
        "valuableGoods": 0,
        "valueLevel": 1,
        "warehouseCode": get_warehouse_code()
    }


def get_item_2():
    return {
        "brand": " 丰田",
        "fragileGoods": 0,
        "itemCode": "1650287",
        "itemName": "空气箱new",
        "ownerCode": "1003399",
        "ownerItemCode": "67003-02500",
        "partsBrand": "123(123)_123",
        "valuableGoods": 0,
        "valueLevel": 1,
        "warehouseCode": get_warehouse_code()
    }


def get_item_3():
    return {
        "brand": " 丰田",
        "fragileGoods": 0,
        "itemCode": "154364",
        "itemName": "大灯",
        "modifiedPartsName": "大灯",
        "ownerCode": "1003399",
        "ownerItemCode": "81561-02420",
        "partsBrand": "富奥",
        "valuableGoods": 0,
        "valueLevel": 1,
        "warehouseCode": get_warehouse_code()
    }
