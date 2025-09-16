# -*- coding: utf-8 -*-
from DemoQADriver.DemoQALib.instances import SELENIUM
from DemoQADriver.DemoQALib.Locators.Elements.checkbox import xpath


class CheckBox():

    def navigate_to_page(self):
        SELENIUM.click_element(xpath['check_box'])
