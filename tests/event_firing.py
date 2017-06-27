import pytest
import time
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    driver.find_element_by_css_selector("h3.r").click()
    #WebDriverWait(driver, 3).until(ec.title_is("webdriver - Пошук Google"))


class MyListener(AbstractEventListener):
    def before_quit(self, driver):
        print("Finished")

    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)
        driver.get_screenshot_as_file('screen' + str(round(time.time() * 1000)) + '.png')






