from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@given('launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.wait = WebDriverWait(context.driver,20)
    
@when('go to brightmoney website')
def step_impl(context):
    context.driver.get("https://dev.brightmoney.co/")
    context.driver.implicitly_wait(20)

@Then("verify text present on the page")
def step_impl(context):
    status = context.driver.find_element_by_xpath("//div[@aria-label='lbl_signup']").is_displayed()
    assert status is True

@Then("close browser")
def step_impl(context):
    context.driver.close()
    
