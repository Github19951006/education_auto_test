"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/05
@File   :student_operation.py
"""
from hytest import *
from cfg.cfg import *
from lib.webUI.yjyx_webui_student_operation import student_operation
from lib.api.yjyx_student_api import gs_student


class Case_tc005081:
	name = '老师登录1 - tc005081'
	
	# 清除方法
	def teardown(self):
		gs_student.del_students(self.studentID)
		student_operation.close_chrome()
	
	def teststeps(self):
		
		# 测试步骤如下
		STEP(1, '创建一个学生')
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'student_yuer', '精锐', SENIOR_THREE_GRADE_ID, cid, '13451813456')
		
		retcode = result_add_student.json()['retcode']
		
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.studentID = result_add_student.json()['id']
		
		CHECK_POINT('检查返回创建成功码', retcode == 0)
		
		STEP(2, '登录学生系统')
		student_operation.student_login('student_yuer')
		home_page_info_list = student_operation.get_home_page_info()
		INFO(home_page_info_list)
		# 获取注册码
		expected = ['精锐', '白月学院00002', f'{home_page_info_list[-3]}', '0', '0']
		CHECK_POINT('检查首页信息',expected == home_page_info_list)
		
		STEP(3, '点击 错题库 菜单')
		wrong_question_lib_info = student_operation.get_wrong_question_lib_info()
		INFO(wrong_question_lib_info)
		expected = '您尚未有错题入库哦'
		CHECK_POINT('检查错题入库信息', wrong_question_lib_info == expected)
