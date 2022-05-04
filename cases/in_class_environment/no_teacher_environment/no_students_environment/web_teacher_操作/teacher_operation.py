"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/03
@File   :teacher_operation.py
"""
from hytest import *
from cfg.cfg import *
from lib.api.yjyx_teacher_api import gs_teacher
from lib.webUI.yjyx_webui_teacher_operation import teacher_operation
from lib.api.yjyx_class_api import gs_class

class Case_tc005001:
	name = '老师登录web系统 - tc005001'
	
	# 清除方法
	def teardown(self):
		gs_teacher.del_teachers(self.addTeacherId)
	
	def teststeps(self):
		# 班级id
		cid = GSTORE['id']
		
		# 测试步骤如下
		STEP(1, '添加老师')
		res_add_teacher = gs_teacher.add_teachers('web_yuer', '文跃锐',
		                                          SUBJECT_ID_JUNIOR_MATH, str(cid),
		                                          '13553896530', 'yuerwen@123.com',
		                                          '32092519830907899')
		ret_add_teacher_json_obj = res_add_teacher.json()
		
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.addTeacherId = ret_add_teacher_json_obj['id']
		CHECK_POINT('检查返回码信息', ret_add_teacher_json_obj['retcode'] == 0)
		
		STEP(2, '老师登录 web系统')
		teacher_operation.teacher_login('web_yuer')
		info_list = teacher_operation.get_home_page_info()
		expected = ['白月学院00002', '文跃锐', '初中数学', '0', '0', '0']
		CHECK_POINT('检查首页信息',expected == info_list)
		teacher_operation.close_chrome() # 关闭浏览器
		
		