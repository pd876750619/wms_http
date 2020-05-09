location_code = 'kw002'
arrival_notice_code = None
warehouse_code = 'BTL_001'
environment = "http://docker36-wmszy.qipeipu.net/btr-wms-admin/"
# environment = "http://192.168.16.32:8080/btr-wms-admin/"
need_put_arrival = True
wave_template_id = "5e93c5fd04014d0012209fae"  # 广州仓波次模板
outbound_num = 10
arrival_num = 1000


# 全局
def get_warehouse_code():
    global warehouse_code
    return warehouse_code


def get_environment():
    global environment
    return environment


# 入库
def get_arrival_notice_code():
    global arrival_notice_code
    return arrival_notice_code


def get_arrival_num():
    global arrival_num
    return arrival_num


def get_location_code():
    global location_code
    return location_code


def get_need_put_arrival():
    global need_put_arrival
    return need_put_arrival


# 出库
def get_wave_template_id():
    global wave_template_id
    return wave_template_id


def get_outbound_num():
    global outbound_num
    return outbound_num
