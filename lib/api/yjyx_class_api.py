"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/20
@File   :yjyx_class_api.py.py
"""
import requests
from cfg.cfg import *
from lib.response.response import *

class classApi:
	# 列出班级
	def list_class(self,gradeid=None):
		
		# 请求体内容
		params = {
			'vcode': g_vcode,
			'action' : 'list_classes_by_schoolgrade'
		}
	
		if gradeid is not None:
			params['gradeid'] = gradeid
			
		res = requests.get(g_api_url_class, params =params)
		
		# 响应消息
		responseData(res)
		return res
	
	# 添加班级
	def add_class(self, gradeid,name,studentlimit):
		
		# 请求体内容
		payload = {
			'vcode': g_vcode,
			'action' : 'add',
			'grade' : gradeid,
			'name' : name,
			'studentlimit' : studentlimit
		}
		
		# data : 表示表单格式
		# json : 表示json格式
		res = requests.post(g_api_url_class,data=payload)
		
		# 响应消息
		responseData(res)
		return res
	
	# 修改班级
	def modify_class(self, classid,name,studentlimit):
		
		# 请求体内容
		payload = {
			'vcode': g_vcode,
			'action': 'modify',
			'name': name,
			'studentlimit': studentlimit
		}
		
		# data : 表示表单格式
		# json : 表示json格式
		# data : 表示表单格式
		# json : 表示json格式
		url = f'{g_api_url_class}/{classid}'
		res = requests.delete(url, data=payload)
		
		# 响应消息
		responseData(res)
		return res
	
	# 删除班级
	def del_class(self, classid):
		
		# 请求体内容
		payload = {
			'vcode': g_vcode
		}
		
		# data : 表示表单格式
		# json : 表示json格式
		url = f'{g_api_url_class}/{classid}'
		res = requests.delete(url, data=payload)
		
		# 响应消息
		responseData(res)
		return res
	
cs = classApi()
cs.add_class(1,'理工1班',50)
cs.list_class()