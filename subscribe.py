from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import json
import os

PATH = os.path.dirname(os.path.abspath(__file__))

class Subscribe():
    # youtubeアクセス
    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://www.youtube.com/?hl=ja&gl=JP')
        self.driver.implicitly_wait(20)


    # ログイン
    def _login(self, mail_address, password):
        self._click('//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]', interval=1)
        self._send_keys('//*[@id="identifierId"]', mail_address, interval=1)
        self._click('//*[@id="identifierNext"]/div/button/span', interval=1)
        self._send_keys('//*[@id="password"]/div[1]/div/div[1]/input', password, interval=1)
        self._click('//*[@id="passwordNext"]/div/button/span', interval=1)
        self._click('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div/yt-img-shadow', interval=1)
        self.driver.implicitly_wait(20)

    # 急上昇に移動
    def _go_surge(self):
        # メニュー押す
        guide_element = self.driver.find_element(By.ID, "guide-button")
        guide_element.click()

        # 急上昇押す
        surge = self.driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item/yt-formatted-string')
        surge.click()
    # 上から10人登録
    def _subscribe(self):
            
        # urlゲット
        urls = []
        for i in range(1,11):
            name = self.driver.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[4]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[{i}]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/div/yt-formatted-string/a')
            urls.append(name.get_attribute('href'))
        
        # チャンネル登録
        for i in range(10):
            self.driver.get(urls[i])

            self._click('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]', interval=1)

    def _click(self, xpath, interval=0):
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()
        sleep(interval)

    def _click_id(self, id, interval=0):
        button = self.driver.find_element(By.ID, id)
        button.click()
        sleep(interval)

    def _send_keys(self, xpath, text, interval=0):
        output = self.driver.find_element(By.XPATH, xpath)
        output.send_keys(text)
        sleep(interval)

if __name__ == "__main__":

    with open(f'{PATH}/secret.json', 'r') as f:
        user_data = json.load(f)

    subscribe = Subscribe()
    subscribe._login(user_data["mail_address"], user_data["password"])
    subscribe._go_surge()
    subscribe._subscribe()
