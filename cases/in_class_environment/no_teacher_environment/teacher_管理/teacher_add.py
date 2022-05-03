"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/24
@File   :teacher_add.py
"""

from hytest import *
from cfg.cfg import *
from lib.api.yjyx_teacher_api import gs_teacher

class Case_tc001001:
    name = '添加老师1 - tc001001'
    
    # 清除方法
    def teardown(self):
        gs_teacher.del_teachers(self.addTeacherId)
 
    def teststeps(self):
        cid = GSTORE['id']
        INFO(cid)
        # 测试步骤如下
        STEP(1,'添加一个老师')
        res_add_teacher = gs_teacher.add_teachers('yuerwen','python老师',
                           SUBJECT_ID_JUNIOR_MATH,str(cid),'13451813456','jcysdf@123.com',
                           '3209251983090987899')
        ret_add_teacher_json_obj = res_add_teacher.json()
        CHECK_POINT('检查返回码信息',ret_add_teacher_json_obj['retcode'] == 0)
        
        INFO(ret_add_teacher_json_obj['id'])

        # ** 保存id，存到self中，self是实例对象都能访问到的东西
        self.addTeacherId = ret_add_teacher_json_obj['id']

        STEP(2,'列出老师信息')
        res_list_teacher = gs_teacher.list_teachers()
        res_list_teacher_json = res_list_teacher.json()
        # 获取返回老师id
        res_list_teacher_id = res_list_teacher_json['retlist'][0]['id']
        INFO(res_list_teacher_id)
        
        CHECK_POINT('检查添加老师返回的ID信息',self.addTeacherId
                    == res_list_teacher_id)

        
       
