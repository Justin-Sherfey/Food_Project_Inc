"""
functions for scraping grub hub

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
from selenium.webdriver.support.ui import WebDriverWait


URL = 'https://www.grubhub.com/'


"""
navigation function for bringing web scraper to the main page to be scraped
"""
def navigate():
    browser = Chrome(executable_path='./chromedriver')
    browser.get(URL)

    addBar = browser.find_element(By.XPATH, '//*[@id="homepage-logged-out-top"]/ghs-welcome-view/div/div[2]/div[2]/div[2]/ghs-start-order-form/div/div[1]/div/ghs-address-input/div/div/div/input')
    addBar.click()
    addBar.send_keys('92117')
    sleep(1)
    addBar.send_keys(Keys.ENTER)

    try:
        popUp = browser.find_element(By.XPATH, '//*[@id="chiri-modal"]/div/div/div[1]/a')
        popUp.click()
        sleep(1)

    except:
        sleep(1)

    finally:
        clearFilters = WebDriverWait(browser, timeout=5).until(
                lambda b: b.find_element(
                    By.XPATH, '//*[@at-facet-label="Open Now"]'
                    )
                )
        assert 'Open Now' in clearFilters.text
        clearFilters.click()

    return browser


"""
main scraping function,
currently collects name, displayName, and tags
"""
def scrapeFeatured(browser=navigate):
    browser = browser()
    rests = browser.find_elements(By.XPATH, '//*[@class="restaurantCard-search u-line-top u-line--light"]')
    featured = []
    for rest in rests:
        featured.append(rest.text)

    browser.close()

    return featured[0:10]


"""
function for parsing scraped data and formatting it into usable data
"""
def parse(string):
    parts = string.split('\n')
    displayName = parts[0]
    name = helpers.parseName(displayName)
    tags = helpers.parseTags(parts[1])

    return (displayName, name, tags)

navigate()
