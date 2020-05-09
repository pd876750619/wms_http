import time

from base.receipt_config import get_warehouse_code, get_arrival_num
from base.wms_base import kafka_put


def arrival_notice_put():
    topic = "WMS_ARRIVAL_NOTICE_CREATE"
    data = get_value()
    return kafka_put(topic, data)


def get_value():
    time_str = time.time().__str__().replace(".", "")
    order_no = 'TIO2_1003399_' + time_str
    return {
        "arrivalNoticeType": 2,
        "details": [
            {
                "goodsQualityType": "1",
                "itemCode": "154364",
                "itemName": "大灯",
                "ownerItemCode": "81561-02420",
                "scheduledQuantity": get_arrival_num(),
                "sourceDetailNo": "TIO2D_1003399_612374"
            },
            {
                "goodsQualityType": "1",
                "itemCode": "153494",
                "itemName": "大灯13246",
                "ownerItemCode": "23300-0D060",
                "scheduledQuantity": get_arrival_num(),
                "sourceDetailNo": "TIO2D_1003399_612375"
            },
            {
                "goodsQualityType": "1",
                "itemCode": "1650287",
                "itemName": "空气箱new",
                "ownerItemCode": "67003-02500",
                "scheduledQuantity": get_arrival_num(),
                "sourceDetailNo": "TIO2D_1003399_612376"
            }
        ],
        "originalOrderNo": "",
        "ownerCode": "1003399",
        "remark": "",
        "scheduledArriveTime": 1586275200000,
        "sourceNo": order_no,
        "sourcePlatform": "ERP",
        "warehouseCode": get_warehouse_code()
    }
