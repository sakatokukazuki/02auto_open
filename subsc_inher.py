from selenium.webdriver.common.by import By
import json
import os
from open_youtube import Youtube

PATH = os.path.dirname(os.path.abspath(__file__))

class SubscribeInheritance(Youtube):

    def __init__(self):
        super().__init__()

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
        for i in range(11,15):
            name = self.driver.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[4]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[{i}]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/div/yt-formatted-string/a')
            urls.append(name.get_attribute('href'))
        
        # チャンネル登録
        for i in range(len(urls)):
            self.driver.get(urls[i])

            self._click('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]', interval=1)


if __name__ == "__main__":

    with open(f'{PATH}/secret.json', 'r') as f:
        user_data = json.load(f)

    subscribe = SubscribeInheritance()
    subscribe._login(user_data["mail_address"], user_data["password"])
    subscribe._go_surge()
    subscribe._subscribe()
