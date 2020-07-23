from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

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
    
    try:
        popUp = browser.find_element(By.XPATH, '//*[@id="chiri-modal"]/div/div/div[1]/a')
        popUp.click()
        sleep(1)

    except:
        sleep(1)

    finally:
        clearFilters = browser.find_element(By.XPATH, '//*[@id="ghs-search-results-container"]/div/div[1]/div/ghs-facets/div/div[1]/div/div[2]/a') 
        clearFilters.click()
        sleep(8)
    
    return browser


def scrapeFeatured(browser=navToFeatured()):
    displayNames = browser.find_elements(By.XPATH, '//*[@class="u-text-ellipsis"]')
    featured = []
    for displayName in displayNames:
        text = displayName.text
        featured.append(text)

    browser.close()

    return featured[0:10]

