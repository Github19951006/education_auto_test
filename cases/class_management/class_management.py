"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/22
@File   :class_management.py.py
"""
from hytest import *
from lib.api.yjyx_class_api import g_cs

class Case_tc000001:
	name = '添加班级1 - tc000001'
	
	# 清除方法
	def teardown(self):
		g_cs.del_class(self.addClassId)
	
	def teststeps(self):
		# 测试步骤如下
		STEP(1,'创建一个班级')
		res_add_class = g_cs.add_class(4,'龙山理22班',69)
		retAdd = res_add_class.json()
		CHECK_POINT('添加结果回码',retAdd['retcode'] == 0)
		
		#** 保存id，存到self中，self是实例对象都能访问到的东西
		self.addClassId = retAdd['id']
		
		STEP(2, '列出班级')
		res_list_class = g_cs.list_class(4)
		resList = res_list_class.json()
		
		# 预期结果
		expected = {
		    "gradeid": 4,
		    "retlist": [
		        {
		            "name": "龙山理22班",
		            "grade__name": "高一",
		            "invitecode": retAdd['invitecode'],
		            "studentlimit": 69,
		            "studentnumber": 0,
		            "id": retAdd['id'],
		            "teacherlist": []
		        }
		    ],
		    "retcode": 0
		}
		CHECK_POINT('列出结果检查', resList == expected)

	