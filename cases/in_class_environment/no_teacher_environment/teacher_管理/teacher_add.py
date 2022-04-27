"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/24
@File   :teacher_add.py
"""

from hytest import *
from lib.api.yjyx_teacher_api import gs_teacher

class Case_tc001001:
    name = '用例名 - tc001001'
    
    # 清除方法
    def teardown(self):
        gs_teacher.del_teachers(self.addTeacherId)
 
    def teststeps(self):
        teacher_cid = GSTORE['id']
        INFO(teacher_cid)
        # 测试步骤如下
        STEP(1,'添加一个老师')
        res_add_teacher = gs_teacher.add_teachers('yuerwang','python老师',
                           1,str(teacher_cid),'13451813456','jcysdf@123.com',
                           '3209251983090987899')
        retAdd = res_add_teacher.json()
        CHECK_POINT('检查返回码信息',retAdd['retcode'] == 0)
        
        INFO(retAdd['id'])

        # ** 保存id，存到self中，self是实例对象都能访问到的东西
        self.addTeacherId = retAdd['id']

        STEP(2,'列出老师信息')
        ret = gs_teacher.list_teachers()
        INFO(ret.json()['retlist'])
       
