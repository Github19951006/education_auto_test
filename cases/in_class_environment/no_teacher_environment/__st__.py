"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/23
@File   :__st__.py.py
"""
from hytest import *
from lib.api.yjyx_teacher_api import *

def suite_setup():
	INFO('删除所有老师')
	gs_teacher.del_all_teachers()
