from hytest import *
from lib.api.yjyx_class_api import *
from lib.api.yjyx_teacher_api import *
from lib.api.yjyx_student_api import *
def suite_setup():

    # 依赖关系：必须先删除该班级中所有的学生和老师，才能删除班级。
    
    INFO('初始化 删除所有老师')
    gs_teacher.del_all_teachers()
    INFO('初始化 删除所有学生')
    gs_student.del_all_students()
    INFO('初始化 删除所有班级')
    gs_class.del_all_class()


'''
决定一个自动化用例放在代码目录的什么地方是有什么决定的？
答：用例需求的 初始数据环境
'''