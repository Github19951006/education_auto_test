from hytest import *
from lib.api.yjyx_class_api import *

def suite_setup():
    INFO('初始化 删除所有班级')
    g_cs.del_all_class()
