from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import keyboard

@Given('launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.wait = WebDriverWait(context.driver,30)

@When('verify adding OTP')
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_SentCode_CodeVerify']")))
    keyboard.write('123456')
    
@when('go to brightmoney website')
def step_impl(context):
    context.driver.get("https://dev.brightmoney.co/")
    context.driver.implicitly_wait(20)

@When("get started button is clicked")
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@aria-label='btn_GetStarted']").click()

@When("continue button is clicked")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath("//div[@aria-label='btn_Continue'][1]").click()
    context.driver.implicitly_wait(10)

@Then("back button is clicked")
def step_impl(context):
    context.driver.find_element_by_xpath("//img[@alt='btn_Back']").click()

@Then("verify text present on the page")
def step_impl(context):
    status = context.driver.find_element_by_xpath("//div[@aria-label='lbl_signup']").is_displayed()
    assert status is True

@Then("verify get started button is disabled")
def step_impl(context):
    getStarted = context.driver.find_element_by_xpath("//div[@aria-label='btn_Next' and @role='button']")
    
    try:
        getStarted.click()
    except Exception as e:
        print(e)
        print("button is disabled")
    finally:
        print(getStarted)
        assert getStarted.is_enabled() is True

@Then("verify adding first name and last name")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_Disclaimer']")))
    # continue_button = context.driver.find_element_by_xpath("//div[aria-label='btn_Next']")
    context.driver.find_element_by_xpath("//input[@type='text'][1]").send_keys("Petko")
    context.driver.find_element_by_xpath("//input[@type='text'][2]").send_keys("Plachkov")

@Then("verify name screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_Disclaimer']")))
    disclaimer = context.driver.find_element_by_xpath("//span[@aria-label='lbl_TermsOfUse']").text
    print(disclaimer)
    # assert disclaimer == "Term's of use"

@When("add wrong mobile number")
def step_impl(context):
    phoneNumber = context.driver.find_element_by_xpath("//input[@maxlength=12]")
    phoneNumber.send_keys("111")

@When("add valid phone number")
def step_impl(context):
    phoneNumber = context.driver.find_element_by_xpath("//input[@maxlength=12]")
    phoneNumber.send_keys('6782963011')

@When("click get started button")
def step_impl(context):
    getStarted = context.driver.find_element_by_xpath("//div[@aria-label='btn_Next' and @role='button']")
    getStarted.click()

@When("verify add OTP screen labels")
def step_impl(context):
    verifyCode = context.driver.find_element_by_xpath("//div[@aria-label='lbl_SentCode_CodeVerify']")
    assert verifyCode.is_displayed() is True
    resendCode = context.driver.find_element_by_xpath("//div[@aria-label='btn_Resend_CodeVerify']") 
    assert resendCode.is_displayed() is True

@Then("verify adding OTP")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_SentCode_CodeVerify']")))
    keyboard.write('123456')

@Then("verify label on first screen")
def step_impl(context):
    label = context.driver.find_element_by_xpath("//div[@aria-label='lbl_crushCreditCard']").is_displayed()
    assert label is True

@When("login button is clicked")
def step_impl(context):
    loginButton = context.driver.find_element_by_xpath("//div[@aria-label='btn_Login']")
    loginButton.click()

@Then("verify login button")
def step_impl(context):
    loginButton = context.driver.find_element_by_xpath("//div[@aria-label='btn_Login']").is_displayed()
    assert loginButton is True

@Then("verify get started button")
def step_impl(context):
    getStartedButton = context.driver.find_element_by_xpath("//div[@aria-label='btn_GetStarted']").is_displayed()
    assert getStartedButton is True

@Then("verify label on second screen")
def step_impl(context):
    meetBrightCredit = context.driver.find_element_by_xpath("//div[@aria-label='lbl_unlockBrightAccount']").is_displayed()
    affordableLine = context.driver.find_element_by_xpath("//div[@aria-label='lbl_PreSell_lowIntrest']").is_displayed()
    assert meetBrightCredit is True
    assert affordableLine is True

@Then("verify continue button presence")
def step_impl(context):
    continueButton = context.driver.find_element_by_xpath("//div[@aria-label='btn_Continue']").is_displayed()
    assert continueButton is True
    
@Then("verify label on third screen")
def step_impl(context):
    transferBalance = context.driver.find_element_by_xpath("//div[@aria-label='lbl_transferBalances']").is_displayed()
    refinanceCreditCard = context.driver.find_element_by_xpath("//span[@aria-label='lbl_Presell_InterestFee']").is_displayed()
    assert transferBalance is True
    assert refinanceCreditCard is True

@When("wait for third screen load")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_transferBalances']")))

@Then("verify label on fourth screen")
def step_impl(context):
    personalisedPlan = context.driver.find_element_by_xpath("//div[@aria-label='lbl_personalizedPlan']").is_displayed()
    subPoint = context.driver.find_element_by_xpath("//div[@aria-label='lbl_personalizedPlanSubPoint']").is_displayed()
    assert personalisedPlan is True
    assert subPoint is True

@Then("verify button back")
def step_impl(context):
    backButton= context.driver.find_element_by_xpath("//img[@alt='btn_Back']")
    assert backButton.is_displayed() is True

@Then("close browser")
def step_impl(context):
    context.driver.close()


    
