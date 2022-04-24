"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/20
@File   :yjyx_teacher_api.py
"""
import requests
from cfg.cfg import *
from lib.response.response import *

class teacherApi:
	
	# 列出老师
	def list_teacher(self,subjectid = None):
		# 请求体内容
		params = {
			'vcode': g_vcode,
			'action': 'search_with_pagenation'
		}
		
		if subjectid is not None:
			params['subjectid'] = subjectid
		
		res = requests.get(g_api_url_teacher, params=params)
		
		# 响应消息
		responseData(res)
		return res
		
		# 添加老师
	def add_teacher(self, username, realname,
	                subjectid,classlist,phonenumber,
	                email,idcardnumber):
		
		# 请求体内容
		payload = {
			'vcode': g_vcode,
			'action': 'add',
			'username':username,
			'realname':realname,
			'subjectid':subjectid,
			'classlist':classlist,
			'phonenumber':phonenumber,
			'email':email,
			'idcardnumber':idcardnumber
		}
		
		# data : 表示表单格式
		# json : 表示json格式
		res = requests.post(g_api_url_teacher, data=payload)
		# 响应消息
		responseData(res)
		return res
		
	# 修改班级
	def modify_class(self, teacherid, realname, studentlimit):
		
		# 请求体内容
		payload = {
			'vcode': g_vcode,
			'action': 'modify',
			'realname': realname,
			'studentlimit': studentlimit
		}
		
		# data : 表示表单格式
		# json : 表示json格式
		url = f'{g_api_url_teacher}/{teacherid}'
		res = requests.put(url, data=payload)
		
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
		url = f'{g_api_url_teacher}/{classid}'
		res = requests.delete(url, data=payload)
		
		# 响应消息
		responseData(res)
		return res
	
	# 删除所有班级
	def del_all_class(self):
		res = self.list_class()
		retObj = res.json()
		for one in retObj['retlist']:
			self.del_class(one['id'])
			
if __name__ == '__main__':
    gs_teacher = teacherApi()
    gs_teacher.add_teacher('yuerwen','文跃锐',
                           1,'[{"id":20337}]',13451813456,'jcysdf@123.com',
                           3209251983090987899)
    gs_teacher.list_teacher()