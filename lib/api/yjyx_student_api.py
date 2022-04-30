"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/20
@File   :yjyx_student_api.py.py
"""

from hytest import *
import requests
from cfg.cfg import *
from lib.response.response import *

class studentApi:
	# 列出学生
	def list_students(self,gradeid=None):
		
		# 请求体内容
		params = {
			'vcode': g_vcode,
			'action' : 'search_with_pagenation'
		}
	
		res = requests.get(g_api_url_students, params =params)
		
		# 响应消息
		responseData(res)
		return res
	
	# 添加学生
	def add_students(self, username,realname,gradeid,classid,phonenumber):
		
		# 请求体内容
		payload = {
			'vcode': g_vcode,
			'action' : 'add',
			'username' : username,
			'realname' : realname,
			'gradeid' : gradeid,
            'classid' : classid,
            'phonenumber' : phonenumber
		}
		
		# data : 表示表单格式
		# json : 表示json格式
		res = requests.post(g_api_url_students,data=payload)
		# 响应消息
		responseData(res)
		return res
	
	# 修改学生
	def modify_students(self, studentid,realname,phonenumber):
		
		# 请求体内容
		payload = {
			'vcode': g_vcode,
			'action': 'modify',
			'realname': realname,
			'phonenumber': phonenumber
		}
		
		# data : 表示表单格式
		# json : 表示json格式
		url = f'{g_api_url_students}/{studentid}'
		res = requests.put(url, data=payload)
		
		# 响应消息
		responseData(res)
		return res
	
	# 删除学生
	def del_students(self, studentid):
		
		# 请求体内容
		payload = {
			'vcode': g_vcode
		}
		
		# data : 表示表单格式
		# json : 表示json格式
		url = f'{g_api_url_students}/{studentid}'
		res = requests.delete(url, data=payload)
		
		# 响应消息
		responseData(res)
		return res
	
	# 删除所有学生
	def del_all_students(self):
		result_list_students = self.list_students()
		students_obj = result_list_students.json()
		for student_obj in students_obj['retlist']:
			self.del_students(student_obj['id'])
			

gs_student = studentApi()

if __name__ == '__main__':
    pass
