"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/03
@File   :yjyx_webui_teacher_operation.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from cfg.cfg import *
import time
class TeacherOperation:
	
	# 教师登录
	def teacher_login(self,username,password = '888888'):
		'''
		教师登录函数
		:param username: 登录名
		:param password: 密码
		:return: 没有返回值
		'''
		self.web_driver = webdriver.Chrome()
		self.web_driver.implicitly_wait(5)
		self.web_driver.get(g_web_url_teacher)
		
		# 键入用户名和密码
		self.web_driver.find_element(By.ID,'username').send_keys(username)
		self.web_driver.find_element(By.ID, 'password').send_keys(password)
		self.web_driver.find_element(By.ID,'submit').click()
		
	def get_home_page_info(self):
		'''
		获取首页信息
		:return:infoList_text  info信息的列表
		'''
		
		self.web_driver.find_element(By.CSS_SELECTOR,
		                             '.main-menu a[href="#/home"] li'
		                             ).click()
		time.sleep(1)
		
		info_elements = self.web_driver.find_elements(By.CSS_SELECTOR,
		                             '#home_div .ng-binding')
		
		return [info_element.text for info_element in info_elements]
		
teacher_operation = TeacherOperation()
if __name__ == '__main__':
	teacher_operation.teacher_login('yue')
	infoList_text = teacher_operation.get_home_page_info()
	print(infoList_text)