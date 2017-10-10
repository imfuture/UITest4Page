#coding=utf-8
'''
Created on 2017年5月17日

@author: derek
'''

from public.common import basepage
from config.globalparam import Env_Url

class viploginPage(basepage.Page):
    '''
    登录页面
    '''
    def into_login_page(self):
        """打开会员登录页面"""
        self.dr.open(Env_Url)

    def input_username(self,values):
        """输入用户名"""
        self.dr.clear_type('name->username',values)

    def input_password(self,values):
        """输入密码"""
        self.dr.clear_type('name->password',values)
        
    def click_login_button(self):
        """点击登录按钮"""
        self.dr.click('css->button.btn.blue.pull-right')#/html/body/div[3]/form/div[3]/button  body > div.content > form > div.form-actions > button

    def return_title(self):
        """返回浏览器标题"""
        return self.dr.get_title()
    
    def click_add_button(self):
        """点击增加按钮"""
        self.dr.click('css->div.addbtn')
