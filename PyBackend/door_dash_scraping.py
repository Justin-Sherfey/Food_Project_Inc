"""
functions for scraping door dash

includes:
navigation
scraping
parsing
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import helpers


# global constants
URL = 'https://www.doordash.com/en-US'


def navigate(start, zipCode):
    browser = Chrome(executable_path='./chromedriver')
    browser.get(start)

    addBar = WebDriverWait(browser, timeout=5).until(
            lambda b: b.find_element(
                By.XPATH, '//*[@placeholder="Enter delivery address"]'
                )
            )
    sleep(1)

    addBar.click()
    addBar.send_keys(zipCode)
    sleep(1)
    addBar.send_keys(Keys.ENTER)
    sleep(5)

    return browser


def scrape(browser):
    allRests = WebDriverWait(browser, timeout=5).until(
            lambda b: b.find_element(
                By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div[5]/div/div[2]'
                )
            )

    rests = WebDriverWait(allRests, timeout=5).until(
            lambda a: a.find_elements(
                By.XPATH, '//*[@data-anchor-id="StoreCard"]'
                )
            )

    displayNames = list(map(lambda e: e.text, rests))

    return displayNames



print(scrape(navigate(URL, '92117')))

