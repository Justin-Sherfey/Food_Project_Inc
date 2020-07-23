from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


URL = 'https://www.ubereats.com/'


def navToFeatured():
    browser = Chrome(executable_path='./chromedriver')
    browser.get(URL)

    addBar = browser.find_element(By.XPATH, '//*[@id="location-typeahead-home-input"]')
    addBar.click()
    addBar.send_keys('92117')
    sleep(1)
    findFood = browser.find_element(By.XPATH, '//*[@id="wrapper"]/main/div[1]/div[2]/div/button')
    findFood.click()
    sleep(8)

    popular = browser.find_element(By.XPATH, '//*[@class="bm bn bo e7"]')
    popular.click()
    sleep(5)

    return browser


def scrapeFeatured(browser=navToFeatured()):
    displayNames = browser.find_elements(By.TAG_NAME, "h3")
    featured = []
    for displayName in displayNames:
        text = displayName.text 
        featured.append(text)
    
    browser.close()

    return featured

