"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/20
@File   :yjyx_teacher_api.py
"""
import requests,json
from cfg.cfg import *
from lib.response.response import *

class teacherApi:
	
	# 列出老师
	def list_teachers(self,subjectid = None):
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
	def add_teachers(self, username, realname,
	                subjectid,class_list_id,phonenumber,
	                email,idcardnumber):
		
		id_list = class_list_id.split(',')
		# 结果还是数据对象
		classlist = [{'id':int(cid.strip())} for cid in id_list]
		print(classlist)
		# 请求体内容
		payload = {
			'vcode': g_vcode,
			'action': 'add',
			'username':username,
			'realname':realname,
			'subjectid':subjectid,
			# 要的是json格式的字符串
			# dumps 方法将数据对象序列化为 json格式的字符串
			'classlist':json.dumps(classlist),
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
		
	# 修改老师
	def modify_teachers(self, teacherid, realname,
	 class_list_id, phonenumber, email, idcardnumber, subjectid = None):
		
		id_list = class_list_id.split(',')
		classlist = [{"id": int(cid.strip())} for cid in id_list]
		
		# 请求体内容
		payload = {
			'vcode': g_vcode,
			'action': 'modify',
			'realname': realname,
			# 'subjectid':subjectid,
			'classlist':json.dumps(classlist),
			'phonenumber':phonenumber,
			'email':email,
			'idcardnumber':idcardnumber
		}
		if subjectid is not None:
			payload['subjectid'] = subjectid
	
		
		# data : 表示表单格式
		# json : 表示json格式
		url = f'{g_api_url_teacher}/{teacherid}'
		res = requests.put(url, data=payload)
		
		# 响应消息
		responseData(res)
		return res
	
	# 删除老师
	def del_teachers(self, teacherid):
		
		# 请求体内容
		payload = {
			'vcode': g_vcode
		}
		
		# data : 表示表单格式
		# json : 表示json格式
		url = f'{g_api_url_teacher}/{teacherid}'
		res = requests.delete(url, data=payload)
		
		# 响应消息
		responseData(res)
		return res
	
	# 删除所有老师
	def del_all_teachers(self):
		res = self.list_teachers()
		retObj = res.json()
		for one in retObj['retlist']:
			self.del_teachers(one['id'])

# 实例一个老师实例对象
gs_teacher = teacherApi()
if __name__ == '__main__':
	gs_teacher.add_teachers(
		'yue','李牛22','5','20269',
		'134518156','jcysdf@123.com',
		'3209251983090987899')
	gs_teacher.list_teachers()
	


