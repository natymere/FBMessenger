from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains

import time
from Constant import FBConstant

# POC
def getElement(driver, strategy, searchItem):
    element = None
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((strategy, searchItem)))
    finally:
        return element


def chrome(headless=False, uaRandom=False):
    opt = webdriver.ChromeOptions()

    if uaRandom:
        ua = UserAgent()
        userAgent = ua.random
        opt.add_argument(f"user-agent={userAgent}")

    if headless:
        opt.add_argument("--headless")

    # support to get response status and headers
    d = webdriver.DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}

    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--disable-notifications")
    # opt.add_argument("window-size=1500,1200")
    # disable notifications
    # prefs = {"profile.managed_default_content_settings.images": 2,
    #          'notifications': 2,
    #          }
    # opt.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome('./chromedriver', options=opt, desired_capabilities=d)
    browser.implicitly_wait(10)
    browser.set_page_load_timeout(20)
    return browser


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def main():
    driver = chrome()
    driver.get(FBConstant.FB_URL)

    username = getElement(driver, By.ID, FBConstant.FB_LOGIN_USERNAME_ID)
    password = getElement(driver, By.ID, FBConstant.FB_LOGIN_PASSWORD_ID)
    submit = getElement(driver, By.ID, FBConstant.FB_LOGIN_BUTTON_ID)

    username.send_keys(FBConstant.FB_USER)
    password.send_keys(FBConstant.FB_PASS)
    submit.click()

    time.sleep(2)
    # go to message url
    driver.get(FBConstant.FB_CONVERSATION_URL)
    time.sleep(2)

    iFrames = driver.find_elements_by_tag_name('iframe')
    print("No of frames present in the web page are: ", len(iFrames))
    firsIframe = iFrames[0]
    driver.switch_to_frame(firsIframe)
    driver.implicitly_wait(3)

    # highlight the contents of the selected iframe
    textbox = getElement(driver, By.CLASS_NAME, FBConstant.FB_TEXTBOX)

    actions = ActionChains(driver)
    actions.move_to_element(textbox)
    actions.click(textbox)

    actions.send_keys(FBConstant.FB_MESSAGE_TO_SEND)
    actions.perform()

    # reset actions - not working
    actions = ActionChains(driver)

    # find send button
    button = getElement(driver, By.XPATH, FBConstant.FB_SEND_BUTTON_XPATH)
    actions.move_to_element(button)
    actions.click(button)
    actions.perform()

    pause()
    driver.close()


if __name__ == '__main__':
    main()
