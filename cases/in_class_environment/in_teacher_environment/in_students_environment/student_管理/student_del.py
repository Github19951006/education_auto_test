"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/01
@File   :student_add.py
"""
import hytest
from lib.api.yjyx_student_api import *

class Case_tc002081:
	name = '删除学生1 - tc002081'
		
	def teststeps(self):
		
		STEP(1,'创建一个学生')
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'sanLi','阿三',SENIOR_THREE_GRADE_ID,cid,'13451813456')
		
		retcode = result_add_student.json()['retcode']
		INFO(result_add_student.json())
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']
		CHECK_POINT('检查返回创建成功码',retcode == 0)
		
		STEP(2, '删除存在的学生ID号')
		gs_student.del_students(self.studentID)
		
		STEP(2,'列出学生信息')
		result_list_students = gs_student.list_students()
		old_student_obj = result_list_students.json()['retlist'][-1]
		CHECK_POINT('检查返回结果id是否一致',
		            old_student_obj['id'] != self.studentID)

	