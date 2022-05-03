"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/28
@File   :teacher_add.py.py
"""

from hytest import *
from cfg.cfg import *
from lib.api.yjyx_teacher_api import gs_teacher
from lib.api.yjyx_class_api import gs_class

class Case_tc001051:
	name = '修改老师1 - tc001051'
	
	def teststeps(self):
		cid = GSTORE['id']
		INFO(cid)
		# 测试步骤如下
		STEP(1, '修改一个老师')
		res_modify_teacher = gs_teacher.modify_teachers(435,'初始化老师',SUBJECT_ID_JUNIOR_MATH,
		                                                str(cid), '13451813456', 'jcysdf@123.com',
		                                                '3209251983090987899')
		
		ret_modify_teacher_json_obj = res_modify_teacher.json()
		INFO(ret_modify_teacher_json_obj)
		CHECK_POINT('检查返回码信息', ret_modify_teacher_json_obj['retcode'] == 1)
		
		expected = {'reason': 'id 为`435`的老师不存在', 'retcode': 1}
		CHECK_POINT('检查返回码信息', ret_modify_teacher_json_obj == expected)


class Case_tc001052:
	name = '修改老师2（修改真实名和授课班级,' \
	       '授课班级原来是1个班，改为两个班） - tc001052'
	
	# 清除方法
	def teardown(self):
		teacher_id = GSTORE['teacher_id']
		cid = GSTORE['id']
		gs_class.del_class(self.addClassId)
		gs_teacher.modify_teachers(teacher_id, '初始化老师',
		                           SUBJECT_ID_JUNIOR_MATH, f'{cid}',
		                           '13451813456', 'jcysdf@123.com',
		                           '3209251983090987899')
	
	def teststeps(self):
		teacher_id = GSTORE['teacher_id']
		cid = GSTORE['id']
		STEP(1, '创建一个班级')
		res_add_class = gs_class.add_class(SENIOR_TWO_GRADE_ID, '高二龙山理22班', 66)
		ret_jsonObj = res_add_class.json()
		
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.addClassId = ret_jsonObj['id']
		
		STEP(2, '修改老师真实名和授课班级')
		res_modify_teacher = gs_teacher.modify_teachers(teacher_id, '修改初始化老师',
		                                                SUBJECT_ID_JUNIOR_MATH, f'{cid},{self.addClassId}',
		                                                '13451813456', 'jcysdf@123.com','3209251983090987899')
		retcode = res_modify_teacher.json()['retcode']
		CHECK_POINT('检查返回码结果',retcode == 0)
		
		STEP(3, '列出老师信息')
		res_list_teacher = gs_teacher.list_teachers()
		res_list_teacher_json = res_list_teacher.json()
		INFO(res_list_teacher_json)
		expected = {
			'username': 'new_teacher',
			'teachclasslist': [cid, self.addClassId],
			'realname': '修改初始化老师',
			'id': res_list_teacher_json['retlist'][-1]['id'],
			'phonenumber': '13451813456',
			'email': 'jcysdf@123.com',
			'idcardnumber': '3209251983090987899'
		}
		CHECK_POINT('检查修改后老师的信息',res_list_teacher_json['retlist'][-1] == expected)