"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/01
@File   :student_add.py
"""
import hytest
from lib.api.yjyx_student_api import *

# 根据标签挑选
force_tags = ['api添加学生']

class Case_tc002002:
	name = '添加学生2 - tc002002'
	
	# 清除方法
	def teardown(self):
		gs_student.del_students(self.studentID)
		
	def teststeps(self):
		
		STEP(1,'创建一个学生')
		
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'sanLi','李三',SENIOR_THREE_GRADE_ID,cid,'13451813456')
		
		retcode = result_add_student.json()['retcode']
		
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']
		
		CHECK_POINT('检查返回创建成功码',retcode == 0)
		
		STEP(2,'列出学生信息')
		
		result_list_students = gs_student.list_students()
		newAdd_student_obj = result_list_students.json()['retlist'][-1]

		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['id'] == result_add_student.json()['id'])


class Case_tc002003:
	name = '添加学生3 登录名为数字 - tc002003'
	
	# 清除方法
	def teardown(self):
		gs_student.del_students(self.studentID)
	
	def teststeps(self):
		STEP(1, '创建一个学生')
		
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'77', '李三', SENIOR_THREE_GRADE_ID, cid, '13451813456')
		
		retcode = result_add_student.json()['retcode']
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']
		
		CHECK_POINT('检查返回创建成功码', retcode == 0)
		
		STEP(2, '列出学生信息')
		
		result_list_students = gs_student.list_students()
		newAdd_student_obj = result_list_students.json()['retlist'][-1]
		INFO(result_list_students.json()['retlist'][-1]['username'])
		
		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['id'] == result_add_student.json()['id'])


class Case_tc002004:
	name = '添加学生4 登录名为特殊字符 - tc002004'
	
	# 清除方法
	def teardown(self):
		gs_student.del_students(self.studentID)
	
	def teststeps(self):
		STEP(1, '创建一个学生')
		
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			',;、？。', '李三', SENIOR_THREE_GRADE_ID, cid, '13451813456')
		
		retcode = result_add_student.json()['retcode']
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']
		
		CHECK_POINT('检查返回创建成功码', retcode == 1)
		
		STEP(2, '列出学生信息')
		
		result_list_students = gs_student.list_students()
		newAdd_student_obj = result_list_students.json()['retlist'][-1]
		INFO(result_list_students.json()['retlist'][-1]['username'])
		
		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['id'] == result_add_student.json()['id'])


class Case_tc002005:
	name = '添加学生5 登录名为特殊字符 - tc002005'
	
	# 清除方法
	def teardown(self):
		gs_student.del_students(self.studentID)
	
	def teststeps(self):
		STEP(1, '创建一个学生')
		
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'hello', '李三', SENIOR_THREE_GRADE_ID, cid, '13451813456')
		
		retcode = result_add_student.json()['retcode']
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']
		
		CHECK_POINT('检查返回创建成功码', retcode == 0)
		
		STEP(2, '列出学生信息')
		
		result_list_students = gs_student.list_students()
		newAdd_student_obj = result_list_students.json()['retlist'][-1]
		INFO(result_list_students.json()['retlist'][-1]['username'])
		
		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['id'] == result_add_student.json()['id'])


class Case_tc002006:
	name = '添加学生6 登录名为中文 - tc002006'
	
	# 清除方法
	def teardown(self):
		gs_student.del_students(self.studentID)
	
	def teststeps(self):
		STEP(1, '创建一个学生')
		
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'登录名中文', '李三', SENIOR_THREE_GRADE_ID, cid, '13451813456')
		
		retcode = result_add_student.json()['retcode']
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']
		
		CHECK_POINT('检查返回创建成功码', retcode == 1)
		
		STEP(2, '列出学生信息')
		
		result_list_students = gs_student.list_students()
		newAdd_student_obj = result_list_students.json()['retlist'][-1]
		INFO(result_list_students.json()['retlist'][-1]['username'])
		
		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['id'] == result_add_student.json()['id'])


class Case_tc002007:
	name = '添加学生7 登录名为英文和数字 - tc002007'
	
	# 清除方法
	def teardown(self):
		gs_student.del_students(self.studentID)
	
	def teststeps(self):
		STEP(1, '创建一个学生')
		
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'hello668', '李三', SENIOR_THREE_GRADE_ID, cid, '13451813456')
		
		retcode = result_add_student.json()['retcode']
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']
		
		CHECK_POINT('检查返回创建成功码', retcode == 0)
		
		STEP(2, '列出学生信息')
		
		result_list_students = gs_student.list_students()
		newAdd_student_obj = result_list_students.json()['retlist'][-1]
		INFO(result_list_students.json()['retlist'][-1]['username'])
		
		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['id'] == result_add_student.json()['id'])


class Case_tc002008:
	name = '添加学生8 登录名为空 - tc002008'
	
	def teststeps(self):
		STEP(1, '创建一个学生')
		
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			None, '李三', SENIOR_THREE_GRADE_ID, cid, '13451813456')
		
		reason = result_add_student.json()['reason']
		INFO(result_add_student.json())
		
		CHECK_POINT('检查返回创建成功码', reason == '缺少参数`username`')

		STEP(2, '列出学生信息')

		result_list_students = gs_student.list_students()
		INFO(result_list_students.json())
		newAdd_student_obj = result_list_students.json()['retlist'][-1]
		INFO(result_list_students.json()['retlist'][-1]['username'])

		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['username'] == 'wuwang')
	
