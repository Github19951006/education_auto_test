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
	INFO('删除所有学生')
	gs_student.del_all_students()