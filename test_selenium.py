from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


def test():
    options = Options()
    options.headless = True

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://demoblaze.com/")
    print(driver.title)
    print(dir(driver))
    sleep(5)
    driver.quit()

    #assert(5==3)

