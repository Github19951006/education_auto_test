"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/20
@File   :response.py.py
"""
# 响应消息
def responseData(response):
	print('------------响应状态码---------------')
	print(response.status_code)
	
	print('------------响应消息头---------------')
	for k, v in response.headers.items():
		print(f'{k}: {v}')
	
	print(' ')
	print('------------响应消息体---------------')
	# obj = json.loads(response.content.decode('utf8'))
	body =response.content.decode('utf8')
	print(body)
	
	try:
		response.json()
	except:
		print('响应消息体不是json格式！！')
	