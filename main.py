import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "Your Chrome Driver PATH or Your Browsers Driver PATH"
TWITTER_ACCOUNT = "ENTER YOUR TWITTER ACCOUNT NAME"
TWITTER_PASSWORD = "ENTER ACCOUNT PASSWORD"
promised_down = 90
promised_up = 10
twitter_link = "https://twitter.com/login"
speed_test_link = "https://speedtest.net/"


class InternetSpeedTwitterBot:

    def __init__(self, path_driver):
        # Initialization of the bot class
        self.driver = webdriver.Chrome(executable_path=path_driver)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # Getting the internet speeds from speedtest website
        self.driver.get(speed_test_link)
        time.sleep(2)
        test = self.driver.find_element_by_class_name("start-button")
        test.click()
        time.sleep(45)
        down_speed = self.driver.find_element_by_class_name("download-speed")
        self.down = float(down_speed.text)
        print(f"Down: {self.down}")
        up_speed = self.driver.find_element_by_class_name("upload-speed")
        self.up = float(up_speed.text)
        print(f"Up: {self.up}")

        # self.driver.quit()

    def tweet_at_provider(self):
        message = f"Hey Internet provider, why is my internet speed {self.down} down/ " \
                  f"{self.up} up when I pay for {promised_down} down/ {promised_up} up?"
        self.driver.get(twitter_link)
        time.sleep(2)

        username = self.driver.find_element_by_name("session[username_or_email]")
        username.send_keys(TWITTER_ACCOUNT)

        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        write_draft = self.driver.find_element_by_class_name("public-DraftStyleDefault-block")
        write_draft.send_keys(message)
        time.sleep(3)

        enter = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span')
        enter.click()

        time.sleep(10)
        self.driver.quit()


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
