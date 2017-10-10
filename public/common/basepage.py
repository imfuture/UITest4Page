#coding=utf-8

class Page(object):
    """
    This is a base page class for Page Object.
    """
    def __init__(self, webdriver_driver):
        self.dr = webdriver_driver