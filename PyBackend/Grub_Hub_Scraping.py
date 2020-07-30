"""
functions for scraping grub hub

includes:
navigation
scraping
parsing
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import helpers


# global constants
URL = 'https://www.grubhub.com/'


"""
navigation function for bringing web scraper to the main page to be scraped
"""
def navigate(zipCode):
    # start browser and navigate to main page
    browser = Chrome(executable_path='./chromedriver')
    browser.implicitly_wait(10)
    browser.get(URL)

    # find address bar > input zip code and hit enter
    addBar = browser.find_element_by_xpath(
            '//*[@id="homepage-logged-out-top"]/ghs-welcome-view/div/div[2]/div[2]/div[2]/ghs-start-order-form/div/div[1]/div/ghs-address-input/div/div/div/input'
            )
    addBar.click()
    addBar.send_keys(zipCode)
    addBar.send_keys(Keys.ENTER)

    # find pop up and clear it
    popUp = browser.find_element_by_xpath(
            '//*[@id="chiri-modal"]/div/div/div[1]/a'
            )
    popUp.click()

    # find filter button and clear it
    clearFilters = browser.find_element_by_xpath(
            '//*[@at-facet-label="Open Now"]'
            )
    clearFilters.click()

    return browser


"""
main scraping function,
currently collects name, displayName, and tags
"""
def scrape(browser):
    # find all restaruants
    rests = WebDriverWait(browser, timeout=5).until(
            lambda b: b.find_elements_by_xpath(
                '//*[@class="restaurantCard-search u-line-top u-line--light"]'
                )
            )

    return list(map(lambda r: r.text, rests))


"""
function for parsing scraped data and formatting it into usable data
"""
def parse(string):
    # split up text soup into parsable parts
    parts = string.split('\n')

    # assign parts to variables
    displayName = parts[0]
    name = helpers.parseName(displayName)
    tags = helpers.parseTags(parts[1])

    return (displayName, name, tags)

