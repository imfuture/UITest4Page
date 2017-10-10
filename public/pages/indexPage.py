#coding=utf-8
'''
@author: derek
'''

from public.common import basepage
from public.common.log import Log

logger = Log()
success = "SUCCESS   "
fail = "FAIL   "

class indexPage(basepage.Page):
    '''
    工作台首页
    '''
    def click_more_button(self):
        """点击增加按钮"""
        self.dr.click('css->div.addBtn')
