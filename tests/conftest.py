import os
from appium import webdriver
import pytest
from screens.calculator_screen import CalculatorScreen


@pytest.fixture(scope="class")
def calculator(request):

    def close_driver():
        driver.quit()


    app_name = "calculator.apk"
    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))


    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['newCommandTimeout'] = 950
    desired_caps['app'] = app_path

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    driver.implicitly_wait(10)

    request.addfinalizer(close_driver)
    calculator = CalculatorScreen(driver)

    return calculator
