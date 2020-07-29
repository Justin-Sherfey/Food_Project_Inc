"""
functions for scraping door dash

includes:
navigation
scraping
parsing
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# global constants
URL = 'https://www.doordash.com/en-US'


def navigate(start, zipCode):
    # start browser and navigate to main page
    browser = Chrome(executable_path='./chromedriver')
    browser.implicitly_wait(10)
    browser.get(start)

    # find address bar > enter zip code and hit enter
    addbar = browser.find_element_by_xpath(
            '//*[@placeholder="Enter delivery address"]'
            )
    addbar.click()
    addbar.send_keys(zipCode)
    addbar.send_keys(Keys.ENTER)
    
    return browser


def scrape(browser):
    # select region with all restaurants
    allRests = WebDriverWait(browser, timeout=5).until(
            lambda b: b.find_element_by_xpath(
                '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div[5]/div/div[2]'
                )
            )

    # select all restaurants
    rests = WebDriverWait(allRests, timeout=5).until(
            lambda a: a.find_elements_by_xpath(
                '//*[@data-anchor-id="StoreCard"]'
                )
            )

    # map restaruants to text soup
    displayNames = list(map(lambda e: e.text, rests))

    return displayNames


def parse(text):


