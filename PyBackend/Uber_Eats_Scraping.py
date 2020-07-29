"""
functions for scraping uber eats

includes:
navigation
scraping
parsing
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# global constants
URL = 'https://www.ubereats.com/'
CHROME_PATH = './chromedriver'
WAIT = 10

"""
navigation function for bringing web scraper to the main page to be scraped
"""
def navigate(zipCode):
    # start browser and navigate to main page
    browser = Chrome(executable_path=CHROME_PATH)
    browser.implicitly_wait(WAIT)
    browser.get(URL)

    # find address bar > input zip and hit enter
    addBar = browser.find_element_by_xpath(
            '//*[@id="location-typeahead-home-input"]'
            )
    addBar.click()
    addBar.send_keys(zipCode)
    addbar.send_keys(Keys.ENTER)

    return browser

"""
main scraping function,
currently collects name, displayName, and tags
"""
def scrape(browser):
    #TODO: add section for navigating to all restaurants
    
    # find all restaurants
    rests = WebDriverWait(browser, timeout=WAIT).until(
            lambda b: b.find_elements_by_xpath(
                '//*[@class="af"]'
                )
            )
    
    # map rests to text soup
    texts = list(map(lambda e: e.text, rests))

    return texts

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

