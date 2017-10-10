#coding=utf-8

import unittest
from time import sleep
from public.common import pyselenium
from config import globalparam
from public.common.log import Log
from public.pages import viploginPage

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    @classmethod
    def setUpClass(self):
        self.logger = Log()
        self.logger.info('######################## This App Cases Start #########################')
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.set_window(1400,900)
        loginpage = viploginPage.viploginPage(self.dr)
        loginpage.into_login_page()
        loginpage.input_username(globalparam.user)
        loginpage.input_password(globalparam.passwd)
        loginpage.click_login_button()
        sleep(3)
        # self.assertIn(u'今目标', self.dr.get_title(), msg='Error!')

    @classmethod
    def tearDownClass(self):
        self.logger = Log()
        self.dr = pyselenium.PySelenium(globalparam.browser)
        print('\n')
        self.dr.quit()
        self.logger.info('######################## This App Cases End ###########################')
