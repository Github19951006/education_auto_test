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
		

class Case_StuAddtc00200X:

	# 修改密码功能的数据驱动
	ddt_cases = [
		{
			'name': '添加学生3 登录名为数字 - tc002003',
			'para': ['dlm', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生4 登录名为特殊字符 - tc002004',
			'para': [',;、？。', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 1]
		},
		{
			'name': '添加学生5 登录名为英文 - tc002005',
			'para': ['hello', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生6 登录名为中文 - tc002006',
			'para': ['中文', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 1]
		},
		{
			'name': '添加学生7 登录名为英文和数字 - tc002007',
			'para': ['dlm688', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生8 登录名为空 - tc002008',
			'para': [None, '李三', SENIOR_THREE_GRADE_ID, '13451813456', 1]
		},
		{
			'name': '添加学生13 登录名为" " - tc0020013',
			'para': [' ', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 1]
		},
		{
			'name': '添加学生9 登录名为长度为1 - tc002009',
			'para': ['h', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生10 登录名为长度为30 - tc0020010',
			'para': ['zaqwsxedcrqazwsxedcrqqqqqqqqqq', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生11 登录名为长度超过为30 - tc0020011',
			'para': ['zaqwsxedcrqazwsxedcrqqqqqqqqqqq', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 1]
		}

	]

	def teardown(self):
		gs_student.del_students(self.studentID)

	def teststeps(self):

		STEP(1, '创建一个学生')

		cid = GSTORE['id']
		# 取出参数(变量解包)
		username, realname, gradeid, phonenumber, status_code = self.para
		result_add_student = gs_student.add_students(
			username, realname, gradeid, cid, phonenumber)

		retcode = result_add_student.json()['retcode']

		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']

		INFO(result_add_student.json())
		CHECK_POINT('检查返回创建成功码', retcode == status_code)

		STEP(2, '列出学生信息')

		result_list_students = gs_student.list_students()
		newAdd_student_obj = result_list_students.json()['retlist'][-1]
		INFO(result_list_students.json()['retlist'][-1]['username'])

		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['id'] == result_add_student.json()['id'])


class Case_StuAddtc00300X:
	# 修改密码功能的数据驱动
	ddt_cases = [
		{
			'name': '添加学生3 真实姓名为数字 - tc003003',
			'para': ['dlm', '23', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生4 真实姓名为特殊字符 - tc003004',
			'para': ['dlm', ',;、？。', SENIOR_THREE_GRADE_ID, '13451813456', 1]
		},
		{
			'name': '添加学生5 真实姓名为英文 - tc003005',
			'para': ['dlm', 'hello', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生6 真实姓名为中文 - tc003006',
			'para': ['dlm', '李三', SENIOR_THREE_GRADE_ID, '13451813456', 1]
		},
		{
			'name': '添加学生7 真实姓名为英文和数字 - tc003007',
			'para': ['dlm', 'dlm688', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生8 真实姓名为空 - tc003008',
			'para': ['dlm', None, SENIOR_THREE_GRADE_ID, '13451813456', 1]
		},
		{
			'name': '添加学生15 真实姓名为" " - tc0030015',
			'para': ['dlm', ' ', SENIOR_THREE_GRADE_ID, '13451813456', 1]
		},
		{
			'name': '添加学生9 真实姓名为长度为1 - tc003009',
			'para': ['dlm', 'h', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生10 真实姓名为长度为30 - tc0030010',
			'para': ['dlm', 'zaqwsxedcrqazwsxedcrqqqqqqqqqq', SENIOR_THREE_GRADE_ID, '13451813456', 0]
		},
		{
			'name': '添加学生11 真实姓名为长度超过为30 - tc0030011',
			'para': ['dlm', 'zaqwsxedcrqazwsxedcrqqqqqqqqqqq', SENIOR_THREE_GRADE_ID, '13451813456', 1]
		},
		{
			'name': '添加学生12 电话号码长度大于11位',
			'para': ['dlm', 'zaq', SENIOR_THREE_GRADE_ID, '134518134561', 1]
		},
		{
			'name': '添加学生13 电话号码长度小于11位 - tc0030011',
			'para': ['dlm', 'za', SENIOR_THREE_GRADE_ID, '134518', 1]
		},
		{
			'name': '添加学生14 电话号码为空 - tc0030011',
			'para': ['dlm', 'za', SENIOR_THREE_GRADE_ID, None, 1]
		}
	]
	
	def teardown(self):
		gs_student.del_students(self.studentID)
	
	def teststeps(self):
		STEP(1, '创建一个学生')
		
		cid = GSTORE['id']
		# 取出参数(变量解包)
		username, realname, gradeid, phonenumber, status_code = self.para
		result_add_student = gs_student.add_students(
			username, realname, gradeid, cid, phonenumber)
		INFO(result_add_student)
		retcode = result_add_student.json()['retcode']
		
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']

		INFO(result_add_student.json())
		CHECK_POINT('检查返回创建成功码', retcode == status_code)
		
		STEP(2, '列出学生信息')
		
		result_list_students = gs_student.list_students()
		newAdd_student_obj = result_list_students.json()['retlist'][-1]
		INFO(result_list_students.json()['retlist'][-1]['realname'])
		
		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['id'] == result_add_student.json()['id'])