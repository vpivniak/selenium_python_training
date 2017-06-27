from selenium.webdriver.support.wait import WebDriverWait


class CustomerListPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(base_url+"/admin/?app=customers&doc=customers")
        return self

    def get_customers_number(self):
        return int(self.driver.find_element_by_css_selector("tfoot tr td").text.split(": ")[1])
