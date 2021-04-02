from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import RemoteCommand


class CalculatorScreen:

    def __init__(self, driver):
        self.driver = driver

    def add_values(self, value_1, value_2):
        self.driver.find_element_by_id(f"digit_{value_1}").click()
        self.driver.find_element_by_id("op_add").click()
        self.driver.find_element_by_id(f"digit_{value_2}").click()

    def divide_values(self, value_1, value_2):
        self.driver.find_element_by_id(f"digit_{value_1}").click()
        self.driver.find_element_by_id("op_div").click()
        self.driver.find_element_by_id(f"digit_{value_2}").click()

    def sub_values(self, value_1, value_2):
        self.driver.find_element_by_id(f"digit_{value_1}").click()
        self.driver.find_element_by_id("op_sub").click()
        self.driver.find_element_by_id(f"digit_{value_2}").click()

    def get_result(self):
        self.driver.find_element_by_accessibility_id("equals").click()
        result = self.driver.find_element_by_id("result_final").text
        result = result.replace("−", "-")
        return result

    def get_result_if_0(self):
        self.driver.find_element_by_accessibility_id("equals").click()
        result = self.driver.find_element_by_id("result_preview").text
        result = result.replace("−", "-")
        return result

    def open_expert_panel(self):
        actions = TouchAction(self.driver)
        actions.tap(x=1030, y=1500)
        actions.perform()

    def close_expert_panel(self):
        actions = TouchAction(self.driver)
        actions.tap(x=315, y=1493)
        actions.perform()
        #self.driver.find_element_by_accessibility_id("arrow").click()


    def clear_result(self):
        dell_button = self.driver.find_element_by_id("del")
        for i in range(3):
            dell_button.click()


    def calculate_sinus(self,value_1, value_2):
        self.open_expert_panel()
        self.driver.find_element_by_accessibility_id("sine").click()
        self.close_expert_panel()
        self.driver.find_element_by_id(f"digit_{value_1}").click()
        self.driver.find_element_by_id(f"digit_{value_2}").click()


