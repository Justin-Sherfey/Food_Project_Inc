"""
functions for scraping uber eats

includes:
navigation
scraping
parsing
"""


from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import helpers
from Restaurant import Restaurant


URL = 'https://www.ubereats.com/'


"""
navigation function for bringing web scraper to the main page to be scraped
"""
def navToFeatured():
    browser = Chrome(executable_path='./chromedriver')
    browser.get(URL)

    addBar = browser.find_element(By.XPATH, '//*[@id="location-\
            typeahead-home-input"]'
            )
    addBar.click()
    addBar.send_keys('92117')
    sleep(1)
    findFood = browser.find_element(By.XPATH, '//*[@id="wrapper"]/\
            main/div[1]/div[2]/div/button'
            )
    findFood.click()
    sleep(10)

    popular = browser.find_element(By.XPATH, '//*[@class="bm bn bo e7"]')
    popular.click()
    sleep(5)

    return browser

"""
main scraping function,
currently collects name, displayName, and tags
"""
def scrapeFeatured(browser=navToFeatured()):
    rests = browser.find_elements(By.XPATH, '//*[@class="af"]')
    featured = []

    for rest in rests:
        featured.append(rest.text)

    browser.close()

    return featured[1:11]

"""
function for parsing scraped data and formatting it into usable data
"""
def parse(string):
    parts = string.split('\n')
    displayName = parts[0]
    if '$' in displayName:
        displayName = parts[1]
    name = helpers.parseName(displayName)
    tags = helpers.parseTags(parts[-1])

    return (displayName, name, tags)

