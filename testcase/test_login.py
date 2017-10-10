#coding=utf-8
'''
@author: derek
'''

from time import sleep
from public.common import mytest
from public.pages import viploginPage
from public.common import datainfo
import unittest

class TestLoginIndex(mytest.MyTest):
    """登录测试"""

    def _login(self,username,password):
        """封装登录函数"""
        loginpage = viploginPage.viploginPage(self.dr)
        loginpage.into_login_page()
        loginpage.input_username(username)
        loginpage.input_password(password)
        loginpage.click_login_button()
        sleep(2)
        self.assertIn(u'今目标', loginpage.return_title())

    def test_login(self):
        """直接登录"""
        loginpage = viploginPage.viploginPage(self.dr)
#         loginpage.into_login_page()
#         loginpage.input_username('admin@1566720')
#         loginpage.input_password('12qwaszx')
#         loginpage.click_login_button()
#         sleep(2)
#         self.assertIn(u'今目标',loginpage.return_title())
# 
#     def test_search_excel(self):
#         """使用数据驱动,进行测试"""
#         datas = datainfo.get_xls_to_list('searKey.xlsx','Sheet1')
#         for data in datas:
#             self._search(data)

if __name__ == '__main__':
    suite = unittest.makeSuite(TestLoginIndex, 'test')
    unittest.TextTestRunner(verbosity=2).run(suite)
