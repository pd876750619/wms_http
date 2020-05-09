import time

from base.wms_arrival_notice import arrival_notice_put
from base.wms_base import token, get_token, switch_warehouse
from base.wms_item import item_put
from base.wms_outbound import do_outbound_wave

from base.wms_receipt import get_wait_receipt, get_wait_receipt_detail, receipt_shelf_inventory, do_receive_shelf
from base.wms_work_config import get_receipt_shelf__config_id

if __name__ == '__main__':
    try:
        # do_receive_shelf()
        do_outbound_wave()
    except Exception as e:
        print('运行异常', e)
