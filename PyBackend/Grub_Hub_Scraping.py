from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import helpers


URL = 'https://www.grubhub.com/'


def navToFeatured():
    browser = Chrome(executable_path='./chromedriver')
    browser.get(URL)

    addBar = browser.find_element(By.XPATH, '//*[@id="homepage-logged-out-top"]/ghs-welcome-view/div/div[2]/div[2]/div[2]/ghs-start-order-form/div/div[1]/div/ghs-address-input/div/div/div/input')
    addBar.click()
    addBar.send_keys('92117')
    sleep(1)
    addBar.send_keys(Keys.ENTER)

    findFood = browser.find_element(By.XPATH, '//*[@id="homepage-logged-out-top"]/ghs-welcome-view/div/div[2]/div[2]/div[2]/ghs-start-order-form/div/div[2]/button')
    findFood.click()
    sleep(5)
    
    try:
        popUp = browser.find_element(By.XPATH, '//*[@id="chiri-modal"]/div/div/div[1]/a')
        popUp.click()
        sleep(1)

    except:
        sleep(1)

    finally:
        clearFilters = browser.find_element(By.XPATH, '//*[@class="ghs-clearAllFacets s-link-dark"]')
        clearFilters.click()
        sleep(8)
    
    return browser


def scrapeFeatured(browser=navToFeatured()):
    rests = browser.find_elements(By.XPATH, '//*[@class="restaurantCard-search u-line-top u-line--light"]')
    featured = []
    for rest in rests:
        featured.append(rest.text)

    browser.close()

    return featured[0:10]


def parse(string):
    parts = string.split('\n')
    displayName = parts[0]
    name = helpers.parseName(displayName)
    tags = helpers.parseTags(parts[1])

    return (displayName, name, tags)

