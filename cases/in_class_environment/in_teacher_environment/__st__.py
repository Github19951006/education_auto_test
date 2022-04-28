"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/28
@File   :__st__.py.py
"""
from hytest import *
from lib.api.yjyx_teacher_api import gs_teacher

def suite_setup():
	teacher_cid = GSTORE['id']
