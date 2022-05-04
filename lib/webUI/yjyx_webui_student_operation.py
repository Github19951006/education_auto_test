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
from hytest import *


class StudentOperation:
	
	# 教师登录
	def student_login(self,username,password = '888888'):
		'''
		学生登录函数
		:param username: 登录名
		:param password: 密码
		:return: 没有返回值
		'''
		# self.web_driver = webdriver.Chrome()
		# self.web_driver.implicitly_wait(5)
		# self.web_driver.get(g_web_url_teacher)
		
		options = webdriver.ChromeOptions()
		options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
		self.web_driver = webdriver.Chrome(options=options)
		self.web_driver.implicitly_wait(5)
		self.web_driver.get(g_web_url_students)
		
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
		                             '.container-fluid .ng-binding')
		
		return [info_element.text for info_element in info_elements]
	
	
	def get_wrong_question_lib_info(self):
		
		'''
		获取错题库信息
		:return: getList_class_student_text 返回学生列表信息
		'''
		elems_main_menu_li = self.web_driver.find_elements(By.CSS_SELECTOR,
		                                                  '.topbar-main .main-menu li')
		
		# 点击错题库
		elems_main_menu_li[-2].click()
	
		# 等待加载列表信息
		# 经验：不加载的情况下报错 StaleElementReferenceException
		time.sleep(1)
		page_wrapper_text = self.web_driver.find_element(By.CSS_SELECTOR,
                                                             '.opacity-level #page-wrapper .row').text
		return page_wrapper_text
		
	
	def close_chrome(self):
		'''
		关闭浏览器
		:return:没有
		'''
		self.web_driver.close()
		
	def web_driver_refresh(self):
		'''
		刷新方法浏览器
		:return: 没有
		'''
		self.web_driver.implicitly_wait(5)
		self.web_driver.refresh()
		
student_operation = StudentOperation()
if __name__ == '__main__':
	student_operation.student_login('jcyrss','sdfsdf5%')
	time.sleep(2)
	teacher_operation.get_class_student_info()
	