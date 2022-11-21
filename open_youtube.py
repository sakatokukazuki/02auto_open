from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import json
import os

PATH = os.path.dirname(os.path.abspath(__file__))

class Youtube():
    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://www.youtube.com/?hl=ja&gl=JP')
        self.driver.implicitly_wait(20)


    def _login(self, mail_address, password):
        self._click('//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]', interval=1)
        self._send_keys('//*[@id="identifierId"]', mail_address, interval=1)
        self._click('//*[@id="identifierNext"]/div/button/span', interval=1)
        self._send_keys('//*[@id="password"]/div[1]/div/div[1]/input', password, interval=1)
        self._click('//*[@id="passwordNext"]/div/button/span', interval=1)
        self._click('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div/yt-img-shadow', interval=1)

    def _click(self, xpath, interval=0):
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()
        sleep(interval)

    def _send_keys(self, xpath, text, interval=0):
        output = self.driver.find_element(By.XPATH, xpath)
        output.send_keys(text)
        sleep(interval)

    def _search_channel(self, input_letters):
        search_el = self.driver.find_element(By.NAME, 'search_query')
        search_el.click()
        search_el.send_keys(input_letters)
        sleep(1)
        enter_el = self.driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon')
        enter_el.click()

        ch_el = self.driver.find_element(By.ID, 'channel-title')
        ch_el.click()
        sleep(1)

    
if __name__ == "__main__":    
    with open(f'{PATH}/secret.json', 'r') as f:
        user_data = json.load(f)
    youtube = Youtube()
    youtube._login(mail_address = user_data["mail_address"], password = user_data["password"])
    youtube._search_channel("kosakae256")
    #get_info(driver)
    #open_lives(driver)
