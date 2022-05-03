"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/01
@File   :student_add.py
"""
import hytest
from lib.api.yjyx_student_api import *

class Case_tc002001:
	name = '添加学生1 - tc002001'
	
	# 清除方法
	def teadown(self):
		gs_student.del_students(self.studentID)
		
	def teststeps(self):
		
		STEP(1,'创建一个学生')
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'sanLi','李三',SENIOR_THREE_GRADE_ID,cid,'13451813456')
		
		retcode = result_add_student.json()['retcode']
		INFO(retcode)
		CHECK_POINT('检查返回创建成功码',retcode == 0)
		
		self.studentID = result_add_student.json()['id']
		
		STEP(2,'列出学生信息')
		result_list_students = gs_student.list_students()
		retlist_list_obj = result_list_students.json()['retlist']
		for student in retlist_list_obj:
			CHECK_POINT('检查返回结果id是否一致',
			            student['id'] == result_add_student.json()['id'])
