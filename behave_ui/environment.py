from selenium import webdriver
from behave_ui.pages.main_page import MainPage


def before_feature(context, feature):
    context.browser = webdriver.Chrome()
    context.main_page = MainPage(context.browser)


def after_feature(context, feature):
    context.browser.quit()
