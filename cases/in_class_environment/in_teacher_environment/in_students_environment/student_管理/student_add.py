"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/01
@File   :student_add.py
"""
import hytest
from lib.api.yjyx_student_api import *

class Case_tc002002:
	name = '添加学生2 - tc002002'
	
	# 清除方法
	def teardown(self):
		gs_student.del_students(self.studentID)
		
	def teststeps(self):
		
		STEP(1,'创建一个学生')
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'sanLi','李三',6,cid,'13451813456')
		
		retcode = result_add_student.json()['retcode']
		
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']
		
		CHECK_POINT('检查返回创建成功码',retcode == 0)
		
		STEP(2,'列出学生信息')
		result_list_students = gs_student.list_students()
		newAdd_student_obj = result_list_students.json()['retlist'][-1]

		CHECK_POINT('检查返回结果id是否一致',
		            newAdd_student_obj['id'] == result_add_student.json()['id'])
