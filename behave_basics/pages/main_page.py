from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage:
    search_field_locator = "//input[@data-testid = 'search-bar']"
    search_button_locator = "//button[@type = 'submit']"

    repos_count_locator = "//article[@class='item'][1]/div/h3"
    following_count_locator = "//article[@class='item'][3]/div/h3"
    followers_count_locator = "//article[@class='item'][2]/div/h3"
    gists_count_locator = "//article[@class='item'][4]/div/h3"

    user_name_locator = "//article[contains(@class,'bHWDWn')]//h4"
    user_github_nickname_locator = "//article[contains(@class,'bHWDWn')]//p[contains(text(), '@')]"
    user_description_locator = "//article[contains(@class,'bHWDWn')]/p"
    user_employer_locator = "//article[contains(@class,'bHWDWn')]/div[@class = 'links']/p[1]"
    user_location_locator = "//article[contains(@class,'bHWDWn')]/div[@class = 'links']/p[2]"
    blog_link_locator = "//article[contains(@class,'bHWDWn')]/div[@class = 'links']/a"
    follow_button_locator = "//article[contains(@class,'bHWDWn')]//a[contains(@href, 'github')]"

    followers_locator = "//div[@class = 'followers']/article"

    def __init__(self, browser):
        self.browser = browser

    def input_in_search_filed(self, text):
        self.browser.find_element(By.XPATH, self.search_field_locator).clear()
        self.browser.find_element(By.XPATH, self.search_field_locator).send_keys(text)

    def click_enter_into_search_field(self):
        self.browser.find_element(By.XPATH, self.search_field_locator).send_keys(Keys.ENTER)

    def click_search_button(self):
        self.browser.find_element(By.XPATH, self.search_button_locator).click()

    def get_repos_count(self):
        return self.browser.find_element(By.XPATH, self.repos_count_locator).text

    def get_following_count(self):
        return self.browser.find_element(By.XPATH, self.following_count_locator).text

    def get_followers_count(self):
        return self.browser.find_element(By.XPATH, self.followers_count_locator).text

    def get_gists_count(self):
        return self.browser.find_element(By.XPATH, self.gists_count_locator).text

    def get_user_name(self):
        return self.browser.find_element(By.XPATH, self.user_name_locator).text

    def get_github_nickname(self):
        return self.browser.find_element(By.XPATH, self.user_github_nickname_locator).text

    def get_user_description(self):
        return self.browser.find_element(By.XPATH, self.user_description_locator).text

    def get_user_employer(self):
        return self.browser.find_element(By.XPATH, self.user_employer_locator).text

    def get_user_location(self):
        return self.browser.find_element(By.XPATH, self.user_location_locator).text

    def click_blog_link(self):
        self.browser.find_element(By.XPATH, self.blog_link_locator).click()

    def get_blog_link(self):
        return self.browser.find_element(By.XPATH, self.blog_link_locator).text

    def click_follow_button(self):
        self.browser.find_element(By.XPATH, self.follow_button_locator).click()

    def get_followers_count_from_list(self):
        return len(self.browser.find_elements(By.XPATH, self.followers_locator))


