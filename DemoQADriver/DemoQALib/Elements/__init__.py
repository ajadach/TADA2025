
# -*- coding: utf-8 -*-
from DemoQADriver.DemoQALib.demoqa import SELENIUM
from DemoQADriver.DemoQALib.Locators.main_page import xpath
from DemoQADriver.DemoQALib.Elements.textbox import TextBox
from DemoQADriver.DemoQALib.Elements.checkbox import CheckBox

class elements():

    def __init__(self):
        pass
        self.text_box = TextBox()
        self.check_box = CheckBox()
        # self.WEBTABLES = WebTables()

    def navigate_to_page(self):
        SELENIUM.scroll_element_into_view(xpath['elements'])
        SELENIUM.click_element(xpath['elements'])
