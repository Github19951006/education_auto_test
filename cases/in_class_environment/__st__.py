from hytest import *
from lib.api.yjyx_class_api import *

def suite_setup():
    INFO('创建一个班级')
    res = g_cs.add_class(6,'2015龙山理22班',69)
    INFO(res.json()['id'])
    # 存储 全局共享 数据
    GSTORE['invitecode'] = res.json()['invitecode']
    GSTORE['id'] = res.json()['id']
    
    
# def suite_teardown():
#     cid = GSTORE['id']
#     g_cs.del_class(cid)
#