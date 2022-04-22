from hytest import *
from lib.api.yjyx_class_api import *

def suite_setup():
    INFO('创建一个班级')
    res = g_cs.add_class(6,'龙山理22班',69)
    
    # 存储 全局共享 数据
    GSTORE['invitecode'] = res.json()['invitecode']
    GSTORE['id'] = res.json()['id']
