from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    @property
    def firstname_input(self):
        return self.driver.find_element_by_name("firstname")

    @property
    def lastname_input(self):
        return self.driver.find_element_by_name("lastname")

    @property
    def address1_input(self):
        return self.driver.find_element_by_name("address1")

    @property
    def postcode_input(self):
        return self.driver.find_element_by_name("postcode")

    @property
    def city_input(self):
        return self.driver.find_element_by_name("city")

    @property
    def email_input(self):
        return self.driver.find_element_by_css_selector("main#content [name=email]")

    @property
    def phone_input(self):
        return self.driver.find_element_by_name("phone")

    @property
    def password_input(self):
        return self.driver.find_element_by_css_selector("main#content [name=password]")

    @property
    def confirmed_password_input(self):
        return self.driver.find_element_by_name("confirmed_password")

    @property
    def create_account_button(self):
        return self.driver.find_element_by_name("create_account")

    def open(self,base_url):
        self.driver.get(base_url +"/en/create_account")
        return self

    def select_country(self, country):
        Select(self.driver.find_element_by_css_selector("select[name=country_code]")).select_by_value(country)

    def select_zone(self, zone):
        self.wait.until(lambda d: d.find_element_by_css_selector("select[name=zone_code] option[value=%s]" % zone))
        Select(self.driver.find_element_by_css_selector("select[name=zone_code]")).select_by_value(zone)


