# -*- coding: utf-8 -*-
from DemoQADriver.DemoQALib.instances import SELENIUM
from DemoQADriver.DemoQALib.Locators.Elements.textbox import xpath


class TextBox():

    def navigate_to_page(self):
        SELENIUM.click_element(xpath['text_box'])

    def choose_parameters(self, *params_and_values):
        parameters = params_and_values[::2]
        values = params_and_values[1::2]
        if not parameters or not values:
            raise ValueError("Missing parameters or values.")

        for param, value in zip(parameters, values):
            new_param_name = param.lower().replace(' ', '_')

            if new_param_name in xpath['INPUT']:
                SELENIUM.input_text(xpath['INPUT'][new_param_name], value)
            elif new_param_name in xpath['SELECT']:
                SELENIUM.select_from_list_by_value(xpath['SELECT'][new_param_name], value)
            else:
                raise ValueError(f"Missing support for this param: {param}")
        element = SELENIUM.get_webelement(xpath['BUTTON']['submit'])
        element.location_once_scrolled_into_view
        SELENIUM.click_element(xpath['BUTTON']['submit'])
