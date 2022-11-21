from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

def access_youtube(driver):

    driver.get('https://www.youtube.com/?hl=ja&gl=JP')
    driver.implicitly_wait(20)
    
def open_lives(driver):
    guide_element = driver.find_element(By.ID, "guide-button")
    guide_element.click()

    driver.implicitly_wait(10)

    short_el = driver.find_element(By.XPATH, '//*[@id="items"]/ytd-guide-entry-renderer[2]')
    rank_el = driver.find_element(By.XPATH, '//*[@id="items"]/ytd-guide-entry-renderer[4]')
    
    rank_el.click()

    driver.implicitly_wait(10)

def search_channel(driver, input_letters):
    search_el = driver.find_element(By.NAME, 'search_query')
    search_el.click()
    search_el.send_keys(input_letters)
    sleep(1)
    enter_el = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon')
    enter_el.click()

    ch_el = driver.find_element(By.ID, 'channel-title')
    ch_el.click()
    sleep(1)
    

def get_info(driver):
    out_el = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[7]/div')
    out_el.click()
    subscribers_el = driver.find_element(By.XPATH, '//*[@id="right-column"]/yt-formatted-string[3]')
    start_el = driver.find_element(By.XPATH, '//*[@id="right-column"]/yt-formatted-string[2]')
    start_day = list(start_el.text)
    print(subscribers_el.text, *start_day[:10])


def login(driver, mail_address, password):
    login_el = driver.find_element(By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
    login_el.click()
    sleep(2)
    output = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
    output.send_keys(mail_address)
    sleep(1)
    next = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span')
    next.click()
    sleep(1)
    enter_pass = driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
    enter_pass.send_keys(password)
    sleep(1)
    next2 = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span')
    next2.click()
    sleep(1)
    choise_account = driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div/yt-img-shadow')
    choise_account.click()
    sleep(1)

if __name__ == "__main__":
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    f = open('account1.txt', 'r')

    datalist = f.readlines()
    access_youtube(driver)
    login(driver, "sorehayabai1700@gmail.com", "Kazuki0205")
    search_channel(driver, "kosakae256")
    #get_info(driver)
    #open_lives(driver)

