from browsermobproxy import Server
from selenium import webdriver

server = Server("D:\\dev\\tools\\browsermob-proxy\\bin\\start.bat")
server.start()
proxy = server.create_proxy()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
driver = webdriver.Chrome(chrome_options=chrome_options)

proxy.new_har("google")

driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("webdriver")
driver.find_element_by_name("btnG").click()

print(proxy.har)  # returns a HAR JSON blob


server.stop()
driver.quit()
