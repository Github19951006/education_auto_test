"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/20
@File   :cfg.py
"""
# vcode 设置
g_vcode = '00000004074389951477'

# 服务地址
g_api_server = 'http://192.168.3.22'

# 班级URL
g_api_url_class = g_api_server + '/api/3school/school_classes'

# 老师url
g_api_url_teacher = g_api_server + '/api/3school/teachers'

g_web_url_teacher = g_api_server + '/teacher/login/login.html'
# 学生url
g_api_url_students = g_api_server + '/api/3school/students'


# 学科id定义 (常量一般用大写)
# 初中
SUBJECT_ID_JUNIOR_MATH    = 1
SUBJECT_ID_JUNIOR_SCIENCE = 5
SUBJECT_ID_JUNIOR_ENGLISH = 11
SUBJECT_ID_JUNIOR_PE      = 12

# 高中
SUBJECT_ID_HIGH_CHINESE = 13
SUBJECT_ID_HIGH_MATH    = 14

# 年级id定义 (常量一般用大写)
# 初中
SEVENTH_GRADE_ID = 1
EIGHTH_GRADE_ID  = 2
NINTH_GRADE_ID   = 3

# 高中
SENIOR_ONE_GRADE_ID   = 4
SENIOR_TWO_GRADE_ID   = 5
SENIOR_THREE_GRADE_ID = 6