"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/01
@File   :__st__.py
"""

from hytest import *
from lib.api.yjyx_student_api import *

def suite_setup():
	STEP(1, '创建一个学生')
	cid = GSTORE['id']
	result_add_student = gs_student.add_students(
		'wuwang', '王五', 6, cid, '1345183456')
	
	GSTORE['student_id'] = result_add_student.json()['id']