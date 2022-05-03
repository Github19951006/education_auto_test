from hytest import *
from cfg.cfg import *
from lib.api.yjyx_class_api import gs_class

def suite_setup():
    INFO('创建一个班级')
    res = gs_class.add_class(SENIOR_THREE_GRADE_ID,'2015龙山理22班',69)
    INFO(res.json()['id'])
    
    # 存储 全局共享 数据
    GSTORE['invitecode'] = res.json()['invitecode']
    GSTORE['id'] = res.json()['id']
    
    
def suite_teardown():
    cid = GSTORE['id']
    gs_class.del_class(cid)
