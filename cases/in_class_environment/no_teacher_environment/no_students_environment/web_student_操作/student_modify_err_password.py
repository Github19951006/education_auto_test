"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/12
@File   :student_modify_err_password.py
"""
from hytest import *
from lib.webUI.yjyx_webui_student_operation import student_operation
import time

# 根据标签挑选
force_tags = ['学生登录1','系统测试','UI测试','UI-StuModifExcept000x']

# 套件初始化
def suite_setup():
	student_operation.student_login('student_yuer')

# 套件清除
def suite_teardown():
	student_operation.student_sign_out()

class Case_StuModifExcept000x:
	# 修改密码功能的数据驱动
	'''
	正确用户名 ：student_yuer
	正确密码   ：888888
	'''
	
	ddt_cases = [
		{
			'name': '学生登录  当前密码为空 - UI-StuModify001',
			'para': [None, '12345678', '12345678', '请输入当前使用的密码！！']
		},
		{
			'name': '学生登录 修改密码为空 - UI-StuModify002',
			'para': ['888888', None, 'password', '请输入新密码！！']
		},
		{
			'name': '学生登录 确认密码为空 - UI-StuModify003',
			'para': ['888888', '8888881', None, '新密码和确认密码不同！']
		},
		{
			'name': '学生登录 确认密码为空 - UI-StuModify003',
			'para': [None, None, None, '请输入当前使用的密码！！']
		}
		
		# 备注 后续做成单独的case
		# {
		# 	'name': '学生登录  修改密码长度为21位 - UI-StuModify004',
		# 	'para': ['888888', '123456789012345678901', '123456789012345678901', '新密码超过指定长度']
		# }
	]
	
	def teststeps(self):
		
		# 取出参数(变量解包)
		old_password, password, confirm_password, tips_info = self.para
		
		# 测试步骤如下
		STEP(1, '修改学生密码')
		student_operation.modify_student_password(old_password, password, confirm_password)
		STEP(2, '获取提示信息')
		get_tips_info = student_operation.get_tips_info()
		time.sleep(1)
		CHECK_POINT('检查错误提示信息', get_tips_info == tips_info)
		student_operation.clear_tips_info()
