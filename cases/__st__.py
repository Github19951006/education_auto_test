from hytest import *
from lib.api.yjyx_class_api import *
from lib.api.yjyx_teacher_api import *
from lib.api.yjyx_student_api import *
def suite_setup():
    
    INFO('初始化 删除所有老师')
    gs_teacher.del_all_teachers()
    INFO('初始化 删除所有学生')
    gs_student.del_all_students()
    INFO('初始化 删除所有班级')
    gs_class.del_all_class()
   
