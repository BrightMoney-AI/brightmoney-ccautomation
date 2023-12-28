from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import random

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
    context.driver.find_element(By.XPATH, "//div[@aria-label='btn_GetStarted']").click()
    

@When("continue button is clicked")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Continue'][1]").click()
    context.driver.implicitly_wait(10)

@Then("back button is clicked")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//img[@alt='btn_Back']").click()

@Then("verify text present on the page")
def step_impl(context):
    status = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_signup']").is_displayed()
    assert status is True

@Then("verify get started button is disabled")
def step_impl(context):
    getStarted = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Next' and @role='button']")
    
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
    context.driver.find_element(By.XPATH, "//input[@type='text'][1]").send_keys("Petko")
    context.driver.find_element(By.XPATH, "//input[@type='text'][2]").send_keys("Plachkov")

@Then("verify name screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_Disclaimer']")))
    disclaimer = context.driver.find_element(By.XPATH, "//span[@aria-label='lbl_TermsOfUse']").text
    print(disclaimer)
    # assert disclaimer == "Term's of use"

@When("add wrong mobile number")
def step_impl(context):
    
    phoneNumber = context.driver.find_element(By.XPATH, "//input[@maxlength=12]")
    phoneNumber.send_keys("111")

@When("add valid phone number")
def step_impl(context):
    phoneNumber = context.driver.find_element(By.XPATH, "//input[@maxlength=12]")
    phoneNumber.send_keys("6782963011")

@When("click get started button")
def step_impl(context):
    getStarted = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Next' and @role='button']")
    getStarted.click()

@When("verify add OTP screen labels")
def step_impl(context):
    
    verifyCode = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_SentCode_CodeVerify']")
    assert verifyCode.is_displayed() is True
    
    resendCode = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Resend_CodeVerify']")
    assert resendCode.is_displayed() is True

@Then("verify adding OTP")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_SentCode_CodeVerify']")))
    keyboard.write('123456')

@Then("verify label on first screen")
def step_impl(context):
    
    label = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_crushCreditCard']").is_displayed()
    assert label is True

@When("login button is clicked")
def step_impl(context):
    loginButton = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Login']")
    loginButton.click()

@Then("verify login button")
def step_impl(context):
    loginButton = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Login']").is_displayed()
    assert loginButton is True

@Then("verify get started button")
def step_impl(context):
    getStartedButton = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_GetStarted']").is_displayed()
    assert getStartedButton is True

@Then("verify label on second screen")
def step_impl(context):
    
    meetBrightCredit = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_unlockBrightAccount']").is_displayed()
    affordableLine = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_PreSell_lowIntrest']").is_displayed()
    assert meetBrightCredit is True
    assert affordableLine is True

@Then("verify continue button presence")
def step_impl(context):

    continueButton = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Continue']").is_displayed()
    assert continueButton is True
    
@Then("verify label on third screen")
def step_impl(context):
    transferBalance = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_transferBalances']").is_displayed()
    refinanceCreditCard = context.driver.find_element(By.XPATH, "//span[@aria-label='lbl_Presell_InterestFee']").is_displayed()
    assert transferBalance is True
    assert refinanceCreditCard is True

@When("wait for third screen load")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_transferBalances']")))

@Then("verify label on fourth screen")
def step_impl(context):
    personalisedPlan = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_personalizedPlan']").is_displayed()
    subPoint = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_personalizedPlanSubPoint']").is_displayed()
    assert personalisedPlan is True
    assert subPoint is True

@Then("verify button back")
def step_impl(context):
    backButton= context.driver.find_element(By.XPATH, "//img[@alt='btn_Back']")
    assert backButton.is_displayed() is True

@Then("close browser")
def step_impl(context):
    context.driver.close()

# steps file for funnel

@When("add phone number")   
def step_impl(context):
    phoneNumber = context.driver.find_element(By.XPATH, "//input[@maxlength=12]")
    # phone_number = '+1' + str(random.randint(200, 999)) + str(random.randint(100, 999)) + str(random.randint(1000, 9999))
    phone_number = "6782963011"
    phoneNumber.send_keys(phone_number)

@Then("adding OTP in OTP screen")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_SentCode_CodeVerify']")))
    otpNumber = context.driver.find_element(By.XPATH, "//input[@maxlength=06]")
    otpNumber.send_keys("000000")
    context.driver.implicitly_wait(10)
    
@Then("verify some basic information screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[text()='Let’s start with some basic information']")))
    basicInformationTitle = context.driver.find_element(By.XPATH, "//div[text()='Let’s start with some basic information']")
    try:
        assert  basicInformationTitle.is_displayed() is True  
    except Exception as e:
        print(e)

@Then("enter First Name")
def step_impl(context):
    firstName = context.driver.find_element(By.XPATH, "//div[text()= 'First Name']/../following-sibling::input")
    firstName.send_keys("Petko")
    context.driver.implicitly_wait(50)

@Then("enter Last Name")
def step_impl(context):
    lastName = context.driver.find_element(By.XPATH, "//div[text()= 'Last Name']/../following-sibling::input")
    lastName.send_keys("Plachkov")
    context.driver.implicitly_wait(50)

@Then("verify continue button is clicked")
def step_impl(context):
   continueButton = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Next' and @tabindex='0']")
   if not continueButton.is_displayed():
        continueButton = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Continue' and @tabindex='0']")
        continueButton.click()
   else:
       continueButton.click()    

   try:
        assert continueButton.is_displayed() is True
        continueButton.click() 
   except Exception as e:
        continueButton = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_Continue' and @tabindex='0']")
        try:
            assert continueButton.is_displayed() is True
            continueButton.click()
        except Exception as e:
            print(e)
       

@Then("verify email address screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[text()='Email Address']")))
    emailAddressTitle = context.driver.find_element(By.XPATH, "//div[text()= 'Email Address']")
    try:
        assert  emailAddressTitle.is_displayed() is True  
    except Exception as e:
        print(e)

@Then("enter email address")
def step_impl(context):
    emailAddress = context.driver.find_element(By.XPATH, "//div[text()= 'Email Address (name@mail.com)']/../following-sibling::input")
    emailID = "petko+test6277@brightmoney.co"
    keyboard.write(emailID)
    context.driver.implicitly_wait(50)
  
@Then("verify date of birth screen labels")
def step_impl(context):
    dateOfBirthTitle = context.driver.find_element(By.XPATH, "")

@Then("enter date of birth")
def step_impl(context):
    dateOfBirth = context.driver.find_element(By.XPATH, "//input[@maxlength = 10]")
    enterDateOfBirth = "11/18/1984"
    dateOfBirth.send_keys(enterDateOfBirth)
    context.driver.implicitly_wait(50) 

@Then("verify address screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[text()='Where do you live?']")))
    addressTitle = context.driver.find_element(By.XPATH, "//div[text()='Where do you live?']")
    try:
        assert  addressTitle.is_displayed() is True  
    except Exception as e:
        print(e)
    
@Then("enter address")
def step_impl(context):
    enterAddress = context.driver.find_element(By.XPATH, "//div[text()= 'Enter Address']/../following-sibling::input")
    address_list = ["1600 15th", "1600 15th Troy", "1600 15th Alabama"]
    enterAddress.send_keys(address_list[1])
    tapFirstAddress = context.driver.find_element(By.XPATH, "//div[@aria-label='addr-0']")
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='addr-0']']")))
    try:
        assert tapFirstAddress.is_displayed() is True
        tapFirstAddress.click()
    except Exception as e:
        print(e)    

@Then("verify total debt screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_SingleSelect']")))
    totalDebtTitle = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_SingleSelect']")
    try:
        assert  totalDebtTitle.is_displayed() is True  
    except Exception as e:
        print(e)

@Then("click on one option on total debt screen")
def step_impl(context):
    tapFirstOption = context.driver.find_element(By.XPATH, "//div[@aria-label='surveyOption']")[1]
    try:
        assert  tapFirstOption.is_displayed() is True
        tapFirstOption.click()  
    except Exception as e:
        print(e) 

@Then("verify current credit score screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_SingleSelect']")))
    currentCreditScoreTitle = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_SingleSelect']")
    currentCreditScoreDescTitle = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_SingleSelectDesc']")
    try:
        assert  currentCreditScoreTitle.is_displayed() and currentCreditScoreDescTitle.is_displayed()
    except Exception as e:
        print(e)
   
@Then("click on one option on current credit score screen")
def step_impl(context):
    # for cb user index is [0] and for refi user index is [5]
    tapFirstOption = context.driver.find_element(By.XPATH, "//div[@aria-label='surveyOption']")[0]
    try:
        assert  tapFirstOption.is_displayed() is True
        tapFirstOption.click()  
    except Exception as e:
        print(e)

@Then("verify income screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_FianlQuestionPage']")))
    incomeScreenTitle = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_FianlQuestionPage']")
    incomeScreenDescTitle = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_PinScreenDisclaimer']")
    try:
        assert  incomeScreenTitle.is_displayed() and incomeScreenDescTitle.is_displayed()
    except Exception as e:
        print(e)

@Then("enter income")
def step_impl(context):
    enterIncome = context.driver.find_element(By.XPATH, "//div[text()= 'Your Annual Gross Income']/../following-sibling::input")
    Income = "45000"
    keyboard.write(Income)
    context.driver.implicitly_wait(50)

@Then("verify how did you hear bright screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_WhatImportant']")))
    howDidYouHearScreenTitle = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_WhatImportant']")
    try:
        assert  howDidYouHearScreenTitle.is_displayed() is True  
    except Exception as e:
        print(e)

@Then("click one option in how did you hear bright screen")
def step_impl(context):
    tapFirstOption = context.driver.find_element(By.XPATH, "//div[@aria-label='Google Search']")
    try:
        assert  tapFirstOption.is_displayed() is True
        tapFirstOption.click()  
    except Exception as e:
        print(e)

@Then("verify setup bright account screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[text()='Set up your Bright Account']")))
    setUpBrightAccountTitle = context.driver.find_element(By.XPATH, "//div[text()='Set up your Bright Account']")
    howOftenYouPaidLabel = context.driver.find_element(By.XPATH, "//div[text()='How often do you get paid?']")
    try:
        assert  setUpBrightAccountTitle.is_displayed() and howOftenYouPaidLabel.is_displayed()
    except Exception as e:
        print(e)

@Then("click on once every month option")
def step_impl(context):
    onceEveryMonthOption = context.driver.find_element(By.XPATH, "//div[@aria-label='btn_onceEveryMonth']")
    try:
        assert  onceEveryMonthOption.is_displayed() is True
        onceEveryMonthOption.click()
    except Exception as e:
        print(e)

@Then("verify unlock exclusive benefits screen labels")
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='lbl_meetBrightAccount']")))
    unlockExclusiveBenefitsTitle = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_meetBrightAccount']")
    unlockExclusiveBenefitsLabel = context.driver.find_element(By.XPATH, "//div[@aria-label='lbl_brightAccountBenefits']")
    try:
        assert  unlockExclusiveBenefitsTitle.is_displayed() and unlockExclusiveBenefitsLabel.is_displayed()
    except Exception as e:
        print(e)