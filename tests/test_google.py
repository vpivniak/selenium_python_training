from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.microsoft import IEDriverManager


def test_example():
    #driver = webdriver.Chrome()
    desired_cap = {'browser': 'chrome', 'build': 'First build', 'browserstack.debug': 'true'}
    driver = webdriver.Remote(command_executor='http://yaroslav6:s3WWpCqiG15on7YzZfDH@hub.browserstack.com:80/wd/hub',desired_capabilities=desired_cap)

    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    #WebDriverWait(driver, 3).until(ec.title_is("webdriver - Пошук Google"))
    driver.quit()