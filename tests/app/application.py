from selenium import webdriver
from tests.pages.admin_panel_login_page import AdminPanelLoginPage
from tests.pages.customer_list_page import CustomerListPage
from tests.pages.registration_page import RegistrationPage
from webdriver_manager.chrome import ChromeDriverManager


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://localhost/litecart2"
        self.admin_user = "admin"
        self.admin_password = "admin"
        self.registration_page = RegistrationPage(self.driver)
        self.admin_panel_login_page = AdminPanelLoginPage(self.driver)
        self.customer_list_page = CustomerListPage(self.driver)

    def quit(self):
        self.driver.quit()

    def register_new_customer(self, customer):
        self.registration_page.open(self.base_url)
        self.registration_page.firstname_input.send_keys(customer.firstname)
        self.registration_page.lastname_input.send_keys(customer.lastname)
        self.registration_page.address1_input.send_keys(customer.address)
        self.registration_page.postcode_input.send_keys(customer.postcode)
        self.registration_page.city_input.send_keys(customer.city)
        self.registration_page.select_country(customer.country)
        self.registration_page.select_zone(customer.zone)
        self.registration_page.email_input.send_keys(customer.email)
        self.registration_page.phone_input.send_keys(customer.phone)
        self.registration_page.password_input.send_keys(customer.password)
        self.registration_page.confirmed_password_input.send_keys(customer.password)
        self.registration_page.create_account_button.click()

    def get_customers_number(self):
        if self.admin_panel_login_page.open(self.base_url).is_on_this_page():
            self.admin_panel_login_page.enter_username(self.admin_user).enter_password(self.admin_password).submit_login()
        return self.customer_list_page.open(self.base_url).get_customers_number()
