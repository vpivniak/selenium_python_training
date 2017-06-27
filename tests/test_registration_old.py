import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(ChromeDriverManager().install())
    request.addfinalizer(wd.quit)
    return wd


def test_registration(driver):

    wait = WebDriverWait(driver,4)

    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.get("http://localhost/litecart/admin/?app=customers&doc=customers")
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "tr.footer td")))

    initial_number = driver.find_element_by_css_selector("tr.footer td").text.split(": ")[1]

    print(initial_number)

    driver.get("http://localhost/litecart/en/create_account")
    driver.find_element_by_name("firstname").send_keys("Jack")
    driver.find_element_by_name("lastname").send_keys("Sparrow")
    driver.find_element_by_name("address1").send_keys("5th Street 15")
    driver.find_element_by_name("postcode").send_keys("11111")
    driver.find_element_by_name("city").send_keys("New York")
    driver.find_element_by_name("email").send_keys("jack"+str(round(time.time() * 1000))+"@gmail.com")
    driver.find_element_by_name("phone").send_keys("+1922883772211")

    driver.find_element_by_css_selector("[id ^= select2-country_code]").click()
    driver.find_element_by_css_selector(".select2-results__option[id $= US]").click()

    wait.until(lambda d: d.find_element_by_css_selector("select[name=zone_code] option[value=NY]"))
    Select(driver.find_element_by_css_selector("select[name=zone_code]")).select_by_value("NY")

    driver.find_element_by_name("password").send_keys("******")
    driver.find_element_by_name("confirmed_password").send_keys("******")
    driver.find_element_by_name("create_account").click()

    driver.get("http://localhost/litecart/admin/?app=customers&doc=customers")

    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"tr.footer td")))
    final_number = driver.find_element_by_css_selector("tr.footer td").text.split(": ")[1]

    print(final_number)

    assert int(final_number)-int(initial_number) == 1
