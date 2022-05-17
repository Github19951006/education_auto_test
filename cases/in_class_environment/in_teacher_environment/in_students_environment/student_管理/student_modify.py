"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/17
@File   :student_modify.py
"""
from hytest import *
from lib.api.yjyx_student_api import *

# 根据标签挑选
force_tags = ['修改学生']

class Case_tc009001:
	name = '修改学生真实姓名 - tc009001'
	
	# 清除方法
	def teardown(self):
		gs_student.modify_students(GSTORE['student_id'],'王五','1345183456')
	
	def teststeps(self):
		STEP(1, '修该学生姓名')
		
		gs_student.modify_students(GSTORE['student_id'],'yuerwen','1345183456')
		result_list_students = gs_student.list_students()
		INFO(result_list_students.json())
		retlist_obj = result_list_students.json()['retlist']
		modify_realname = retlist_obj[0]['realname']
		
		STEP(2,'验证修改后的真实姓名')
		CHECK_POINT('判断修改的信息是否生效',modify_realname == 'yuerwen')


class Case_tc009002:
	name = '修改学生电话号码 - tc009002'
	
	# 清除方法
	def teardown(self):
		gs_student.modify_students(GSTORE['student_id'], '王五', '1345183456')
	
	def teststeps(self):
		STEP(1, '修该学生姓名')
		
		gs_student.modify_students(GSTORE['student_id'],'王五','0000000000000')
		result_list_students = gs_student.list_students()
		INFO(result_list_students.json())
		retlist_obj = result_list_students.json()['retlist']
		modify_phonenumber = retlist_obj[0]['phonenumber']
		
		STEP(2, '验证修改后的真实姓名')
		CHECK_POINT('判断修改的信息是否生效', modify_phonenumber == '0000000000000')


class Case_tc009003:
	name = '修改学生电话号码 和 姓名 - tc009003'
	
	# 清除方法
	def teardown(self):
		gs_student.modify_students(GSTORE['student_id'], '王五', '1345183456')
	
	def teststeps(self):
		STEP(1, '修该学生姓名')
		
		gs_student.modify_students(GSTORE['student_id'], '老六', '666888')
		result_list_students = gs_student.list_students()
		INFO(result_list_students.json())
		retlist_obj = result_list_students.json()['retlist']
		modify_realname = retlist_obj[0]['realname']
		modify_phonenumber = retlist_obj[0]['phonenumber']
		
		STEP(2, '验证修改后的真实姓名和电话号码')
		CHECK_POINT('判断修改的信息是否生效', modify_phonenumber == '666888' and  modify_realname == '老六' )


class Case_tc009004:
	name = '修该学生姓名 和 电话号码设置为None - tc009004'
	
	# 清除方法
	def teardown(self):
		gs_student.modify_students(GSTORE['student_id'], '王五', '1345183456')
	
	def teststeps(self):
		STEP(1, '修该学生姓名 和 电话号码设置为None')
		
		gs_student.modify_students(GSTORE['student_id'])
		result_list_students = gs_student.list_students()
		INFO(result_list_students.json())
		retlist_obj = result_list_students.json()['retlist']
		modify_realname = retlist_obj[0]['realname']
		modify_phonenumber = retlist_obj[0]['phonenumber']
		
		STEP(2, '验证修改后的真实姓名和电话号码')
		CHECK_POINT('判断修改的信息是否生效', modify_phonenumber == '1345183456' and modify_realname == '王五')


class Case_tc009005:
	name = '修改学生电话号码为可选值 - tc009006'
	
	# 清除方法
	def teardown(self):
		gs_student.modify_students(GSTORE['student_id'], '王五', '1345183456')
	
	def teststeps(self):
		STEP(1, '修该学生姓名 和 电话号码设置为None')
		
		gs_student.modify_students(GSTORE['student_id'], '王五')
		result_list_students = gs_student.list_students()
		INFO(result_list_students.json())
		retlist_obj = result_list_students.json()['retlist']
		modify_realname = retlist_obj[0]['realname']
		modify_phonenumber = retlist_obj[0]['phonenumber']
		
		STEP(2, '验证修改后的真实姓名和电话号码')
		CHECK_POINT('判断修改的信息是否生效', modify_phonenumber == '1345183456' and modify_realname == '王五')


class Case_tc009006:
	name = '修改学生真实姓名为可选值 - tc009006'
	
	# 清除方法
	def teardown(self):
		gs_student.modify_students(GSTORE['student_id'], '王五', '1345183456')
	
	def teststeps(self):
		STEP(1, '修该学生姓名 和 电话号码设置为None')
		
		gs_student.modify_students(GSTORE['student_id'], phonenumber='8778787878787')
		result_list_students = gs_student.list_students()
		INFO(result_list_students.json())
		retlist_obj = result_list_students.json()['retlist']
		modify_realname = retlist_obj[0]['realname']
		modify_phonenumber = retlist_obj[0]['phonenumber']
		
		STEP(2, '验证修改后的真实姓名和电话号码')
		CHECK_POINT('判断修改的信息是否生效', modify_phonenumber == '8778787878787' and modify_realname == '王五')


class Case_tc009011:
	name = '修改学生id不存在 - tc0090111'
	
	# 清除方法
	def teardown(self):
		gs_student.modify_students(GSTORE['student_id'], '王五', '1345183456')
	
	def teststeps(self):
		STEP(1, '修该的学生id不存在')
		
		gs_student.modify_students(None, '王五', '1345183456')
		result_list_students = gs_student.list_students()
		INFO(result_list_students.json())
		retcode = result_list_students.json()['retcode']
		INFO(retcode)

		STEP(2, '验证修该的学生id不存在情况')
		CHECK_POINT('判断学生id不存在是否异常', retcode == 404)