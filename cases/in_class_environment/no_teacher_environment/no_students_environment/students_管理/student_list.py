"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/19
@File   :student_list.py
"""

from lib.api.yjyx_student_api import *

class Case_ListStu001:
	name = '无学生时列出学生 - ListStu001'
	def teststeps(self):
		result_list_students = gs_student.list_students()
		INFO(result_list_students.json())
		
		expects = {'retlist': [], 'retcode': 0}
		CHECK_POINT('检查服务端会返回信息',result_list_students.json() == expects)