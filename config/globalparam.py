#coding=utf-8

import os
from public.common.readconfig import ReadConfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# 项目参数设置
prj_path = read_config.getValue('projectConfig','project_path')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')
# 默认浏览器
browser = 'chrome'
# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')
# driver路径
driver_path = os.path.join(prj_path, 'driver')
# 环境URL
Env_Url = 'http://vip.kmhealthcloud.com:20002/mxm/login'
#Env_Url = 'http://web.test.com'

# 测试用户名和密码
user = 'admin'
passwd = 'member@2017'