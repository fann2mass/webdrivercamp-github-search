import re
import time
import requests

from behave import *

base_github_url = "https://api.github.com"


@given('Browser: Navigate to {url}')
def navigate_to(context, url):
    context.browser.get(url)


@when('UI: search for "{username}"')
def search_for_username(context, username):
    context.main_page.input_in_search_filed(username)
    context.main_page.click_search_button()


@when('UI: search for "{username}" using enter/return')
def search_for_username_using_enter_return(context, username):
    context.main_page.input_in_search_filed(username)
    context.main_page.click_enter_into_search_field()


@step('API: send GET request "{url}"')
def get_request_followers(context, url):
    token = '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'
    headers = {
        'Authorization': f'token {token}',
    }
    response = requests.get(base_github_url + url, headers=headers)
    context.response = response


@step('API: verify status code is "{status_code}"')
def verify_status_code(context, status_code):
    print(f"Response status code: {context.response.status_code}")
    assert context.response.status_code == int(status_code)


@step("UI: click on blog link")
def click_on_blog_link(context):
    context.main_page.click_blog_link()


@step("UI: click on follow button")
def click_on_follow_button(context):
    context.main_page.click_follow_button()


# Asserts
@then("UI: verify total number of Followers")
def verify_number_of_followers(context):
    expected_number_of_followers = len(context.response.json())
    actual_number_of_followers = int(context.main_page.get_followers_count())
    assert expected_number_of_followers == actual_number_of_followers, f"expected_number_of_followers: {expected_number_of_followers} should be equals with actual_number_of_followers: {actual_number_of_followers}"


@then("UI: verify total number of Following")
def verify_number_of_following(context):
    expected_number_of_following = int(context.response.json()['following'])
    actual_number_of_following = int(context.main_page.get_following_count())
    assert expected_number_of_following == actual_number_of_following, f"expected_number_of_following: {expected_number_of_following} should be equals with actual_number_of_followers: {actual_number_of_following}"


@then("UI: verify total number of Gists")
def verify_number_of_gists(context):
    expected_number_of_gists = int(context.response.json()['public_gists'])
    actual_number_of_gists = int(context.main_page.get_gists_count())
    assert expected_number_of_gists == actual_number_of_gists, f"expected_number_of_gists: {expected_number_of_gists} should be equals with actual_number_of_gists: {actual_number_of_gists}"


@then("UI: verify total number of Repos")
def verify_number_on_repos(context):
    expected_number_of_repos = len(context.response.json())
    actual_number_of_repos = int(context.main_page.get_repos_count())
    assert expected_number_of_repos == actual_number_of_repos, f"expected_number_of_repos: {expected_number_of_repos} should be equals with actual_number_of_repos: {actual_number_of_repos}"


@then("UI: verify user info")
def verify_user_info(context):
    expected_name = context.response.json()['name'] or ''
    expected_nickname = context.response.json()['login'] or ''
    expected_description = context.response.json()['bio'] or ''
    expected_employer = context.response.json()['company'] or ''
    expected_location = context.response.json()['location'] or ''
    expected_blog_link = context.response.json()['blog'] or ''

    actual_name = context.main_page.get_user_name()
    actual_nickname = context.main_page.get_github_nickname()
    actual_description = context.main_page.get_user_description()
    actual_employer = context.main_page.get_user_employer()
    actual_location = context.main_page.get_user_location()
    actual_blog_link = context.main_page.get_blog_link()

    assert expected_name == actual_name,  f"expected_name: {expected_name} should be equals with actual_name: {actual_name}"
    assert expected_nickname.replace('@', '') == actual_nickname.replace('@', ''),  f"expected_nickname: {expected_nickname.replace('@', '')} should be equals with actual_nickname: {actual_nickname.replace('@', '')}"
    assert expected_description.strip() == actual_description.strip(),  f"expected_description: {expected_description.strip()} should be equals with actual_description: {actual_description.strip()}"
    assert expected_employer == actual_employer,  f"expected_employer: {expected_employer} should be equals with actual_employer: {actual_employer}"
    assert expected_location == actual_location,  f"expected_location: {expected_location} should be equals with actual_location: {actual_location}"
    assert expected_blog_link == actual_blog_link,  f"expected_blog_link: {expected_blog_link} should be equals with actual_blog_link: {actual_blog_link}"


@then("Browser: verify blog url")
def verify_blog_url(context):
    expected_blog_link = context.response.json()['blog'] or ''
    browser_url = context.browser.current_url
    assert expected_blog_link == browser_url,  f"expected_blog_link: {expected_blog_link} should be equals with actual_blog_link: {browser_url}"


@then("Browser: verify github url")
def verify_github_url(context):
    expected_github_link = context.response.json()['html_url'] or ''
    browser_url = context.browser.current_url
    assert expected_github_link == browser_url,  f"expected_github_link: {expected_github_link} should be equals with browser_url: {browser_url}"


@then("UI: verify followers, following, repos and gists is zero")
def verify_user_numbers_is_empty(context):
    actual_number_of_followers = int(context.main_page.get_followers_count())
    actual_number_of_following = int(context.main_page.get_following_count())
    actual_number_of_gists = int(context.main_page.get_gists_count())
    actual_number_of_repos = int(context.main_page.get_repos_count())

    assert actual_number_of_repos == 0,  f"actual_number_of_repos: {actual_number_of_repos} should be 0"
    assert actual_number_of_following == 0,  f"actual_number_of_following: {actual_number_of_following} should be 0"
    assert actual_number_of_followers == 0,  f"actual_number_of_followers: {actual_number_of_followers} should be 0"
    assert actual_number_of_gists == 0,  f"actual_number_of_gists: {actual_number_of_gists} should be 0"


@step("UI: verify Followers list is empty")
def verify_followers_list_is_empty(context):
    actual_followers_count_from_list = context.main_page.get_followers_count_from_list()

    assert actual_followers_count_from_list == 0,  f"actual_followers_count_from_list: {actual_followers_count_from_list} should be 0"


@step("UI: verify user data is empty")
def verify_user_data_is_empty(context):
    actual_name = context.main_page.get_user_name()
    actual_nickname = context.main_page.get_github_nickname()
    actual_description = context.main_page.get_user_description()
    actual_employer = context.main_page.get_user_employer()
    actual_location = context.main_page.get_user_location()
    actual_blog_link = context.main_page.get_blog_link()

    assert actual_name == '',  f"actual_name: {actual_name} should be empty"
    assert actual_nickname == '',  f"actual_nickname: {actual_nickname} should be empty"
    assert actual_description == '',  f"actual_description: {actual_description} should be empty"
    assert actual_employer == '',  f"actual_employer: {actual_employer} should be empty"
    assert actual_location == '',  f"actual_location: {actual_location} should be empty"
    assert actual_blog_link == '',  f"actual_blog_link: {actual_blog_link} should be empty"


@then("UI: verify correct number of Followers is displayed in the followers list")
def verify_number_of_followers_in_the_list(context):
    expected_number_of_followers = len(context.response.json())
    time.sleep(2)
    actual_followers_count_from_list = context.main_page.get_followers_count_from_list()

    assert expected_number_of_followers == actual_followers_count_from_list,  f"expected_number_of_followers: {expected_number_of_followers} should be equals with actual_followers_count_from_list: {actual_followers_count_from_list}"


@then("UI: verify number of Followers is 100 in the list")
def verif_number_of_followers_cant_be_more_than_100(context):
    time.sleep(2)
    actual_followers_count_from_list = context.main_page.get_followers_count_from_list()

    assert actual_followers_count_from_list == 100,  f"actual_followers_count_from_list: {actual_followers_count_from_list} should be 100"
