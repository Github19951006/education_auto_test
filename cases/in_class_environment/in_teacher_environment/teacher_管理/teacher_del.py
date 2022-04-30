"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/28
@File   :teacher_add.py.py
"""

from hytest import *
from lib.api.yjyx_teacher_api import gs_teacher
from lib.api.yjyx_class_api import gs_class

class Case_tc001081:
	name = '删除老师1(不存在的老师ID号) - tc001081'
	
	def teststeps(self):
		res_del_teacher = gs_teacher.del_teachers(4545)
		ret_del_teacher_json_obj = res_del_teacher.json()
		expected = {
			"retcode": 404,
			"reason": "id 为`4545`的老师不存在"
		}
		INFO(ret_del_teacher_json_obj)
		CHECK_POINT('检查返回结果',expected == ret_del_teacher_json_obj )

class Case_tc001082:
	name = '删除老师2(存在的老师ID号) - tc001082'
	
	# 清除方法
	def teardown(self):
		gs_teacher.del_teachers(self.addTeacherId )
	
	
	def teststeps(self):
		cid = GSTORE['id']
		# 测试步骤如下
		STEP(1, '添加一个老师')
		res_add_teacher = gs_teacher.add_teachers('add_yuer', '创建老师',
		                                          5, str(cid), '1345181', 'jcysd@123.com',
		                                          '3209251983007899')
		ret_add_teacher_json_obj = res_add_teacher.json()
		INFO(ret_add_teacher_json_obj['id'])
		
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.addTeacherId = ret_add_teacher_json_obj['id']
		
		res_del_teacher = gs_teacher.del_teachers(self.addTeacherId)

		CHECK_POINT('检查删除老师后的结果',res_del_teacher.json()['retcode'] == 0)

		STEP(2, '列出老师信息')
		res_list_teacher = gs_teacher.list_teachers()
		res_list_teacher_json = res_list_teacher.json()
		res_list_teacher_json_id = res_list_teacher_json['retlist'][0]['id']
		INFO(res_list_teacher_json['retlist'][0]['id'])
		CHECK_POINT('检查修改后老师的信息',self.addTeacherId != res_list_teacher_json_id)