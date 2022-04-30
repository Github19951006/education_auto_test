"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/28
@File   :teacher_add.py.py
"""

from hytest import *
from lib.api.yjyx_teacher_api import gs_teacher


class Case_tc001002:
	name = '添加老师2 - tc001002'
	
	# 清除方法
	def teardown(self):
		gs_teacher.del_teachers(self.addTeacherId)
	
	def teststeps(self):
		cid = GSTORE['id']
		INFO(cid)
		# 测试步骤如下
		STEP(1, '添加一个老师')
		res_add_teacher = gs_teacher.add_teachers('new_yuer', '不存在同登录名的老师',
		                                          5, str(cid), '134518136', 'jcysdf@123.com',
		                                          '32092519830907899')
		ret_add_teacher_json_obj = res_add_teacher.json()
		CHECK_POINT('检查返回码信息', ret_add_teacher_json_obj['retcode'] == 0)
		
		INFO(ret_add_teacher_json_obj['id'])
		
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.addTeacherId = ret_add_teacher_json_obj['id']
		
		STEP(2, '列出老师信息')
		res_list_teacher = gs_teacher.list_teachers()
		res_list_teacher_json = res_list_teacher.json()
		# INFO(res_list_teacher_json)
		# 获取返回老师id
		res_list_teacher_id = res_list_teacher_json['retlist'][-1]['id']
		INFO(res_list_teacher_id)

		CHECK_POINT('检查添加老师返回的ID信息', self.addTeacherId
		            == res_list_teacher_id)


class Case_tc001003:
	name = '添加老师3（系统中存在同登录名的老师） - tc001003'
	
	def teststeps(self):
		cid = GSTORE['id']
		INFO(cid)
		# 测试步骤如下
		STEP(1, '添加一个老师')
		res_add_teacher = gs_teacher.add_teachers('new_teacher', '系统中存在同登录名的老师',
		                                          5, str(cid), '13451136', 'jcysd@123.com',
		                                          '32092519830907899')
		ret_add_teacher_json_obj = res_add_teacher.json()
		INFO(ret_add_teacher_json_obj)
		expected = {'reason': '登录名 new_teacher 已经存在', 'retcode': 1}
		CHECK_POINT('检查返回码信息', ret_add_teacher_json_obj == expected)
		
		STEP(2, '列出老师信息')
		res_list_teacher = gs_teacher.list_teachers()
		res_list_teacher_json = res_list_teacher.json()
		
		# 获取返回老师id
		res_list_teacher_realname = res_list_teacher_json['retlist'][-1]['realname']
		INFO(res_list_teacher_realname)
		CHECK_POINT('检查返回老师真实姓名信息',res_list_teacher_realname != '系统中存在同登录名的老师')
	