"""
functions for scraping door dash

includes:
navigation
scraping
parsing
"""
import helpers
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from Restaurant import Restaurant


# global constants
URL = 'https://www.doordash.com/en-US'


"""
function for navigating to scrapable part of site
"""
def navigate(zipCode):
    # start browser and navigate to main page
    browser = Chrome(executable_path='../chromedriver')
    browser.get(URL)

    # find address bar > enter zip code and hit enter
    addbar = WebDriverWait(browser, timeout=5).until(
            lambda b: b.find_element_by_xpath(
                '//*[@placeholder="Enter delivery address"]'
                )
            )
    addbar.send_keys(zipCode)
    sleep(2)
    addbar.send_keys(Keys.ENTER)
    sleep(2)

    return browser


"""
function for scraping raw data from site
"""
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


"""
function for parsing scraped data and formatting it into usable data
"""
def parse(text):
    # split up text soup into parsable parts
    parts = text.split('\n')

    # assign parts to variables
    displayName = parts[0]
    name = helpers.parseName(displayName)
    tags = helpers.parseTags(parts[2])
    rating = helpers.parseRating(parts[-3])

    return Restaurant(displayName, name, tags, rating)

