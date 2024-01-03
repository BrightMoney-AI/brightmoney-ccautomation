#  brew install --cask chromedriver in terminal and 
#  xattr -d com.apple.quarantine $(which chromedriver) in terminal
Feature: Bright Money web screen

    @regression
    Scenario: validate phone number sceeen 
        Given launch Chrome browser
        When go to brightmoney website
        And login button is clicked
        Then verify text present on the page
        And verify get started button is disabled
        And close browser

    @negative
    Scenario: validate adding wrong phone number
        Given launch Chrome browser
        When go to brightmoney website
        And login button is clicked
        And add wrong mobile number
        Then verify get started button is disabled
        And close browser
    
    @regression
    Scenario: validate login functionality on web
        Given launch Chrome browser
        When go to brightmoney website
        And login button is clicked
        And add valid phone number
        And click get started button
        And verify add OTP screen labels
        Then verify adding OTP
        And close browser

    @regression
    Scenario: validate name screen on web
        Given launch Chrome browser
        When go to brightmoney website
        And login button is clicked
        And add valid phone number
        And click get started button
        And verify add OTP screen labels
        Then verify adding OTP
        And verify name screen labels
        And verify adding first name and last name
        And close browser
    

    @regression
    Scenario: validate first screen after URL load
        Given launch Chrome browser
        When go to brightmoney website
        Then verify label on first screen
        And verify login button
        And verify get started button
        And close browser

    @regression
    Scenario: validate second screen after URL load
        Given launch Chrome browser
        When go to brightmoney website
        And get started button is clicked
        Then verify label on second screen
        And verify continue button presence
        And close browser
    
    @regression
    Scenario: validate third screen after URL load
        Given launch Chrome browser
        When go to brightmoney website
        And get started button is clicked
        And continue button is clicked
        Then verify label on third screen
        And verify button back
        And verify continue button presence
        And close browser
    
    @back
    Scenario: validate back button clicked on third screen
        Given launch Chrome browser
        When go to brightmoney website
        And get started button is clicked
        And continue button is clicked
        Then verify label on third screen
        And back button is clicked
        And verify label on second screen
        And close browser
    

    @regression
    Scenario: validate fourth static screen after entering URL
        Given launch Chrome browser
        When go to brightmoney website
        And get started button is clicked
        And continue button is clicked
        And wait for third screen load
        And continue button is clicked
        Then verify label on fourth screen
        And verify button back
        And verify continue button presence
        And close browser


    @Funnel
    Scenario: validate onboarding user till SSN screen
        # Till ssn screen
        Given launch chrome browser
        When go to brightmoney website
        And login button is clicked
        And add phone number
        And click get started button
        And verify add OTP screen labels
        Then adding OTP in OTP screen
        And verify some basic information screen labels
        And enter First Name
        And enter Last Name
        Then verify continue button is clicked
        And verify email address screen labels
        And enter email address
        Then verify continue button is clicked
        And verify Date Of Birth screen labels
        And enter Date Of Birth
        Then verify continue button is clicked
        And verify address screen labels
        And enter address
        Then verify continue button is clicked
        And verify total debt screen labels
        And click on one option on total debt screen
        Then verify continue button is clicked 
        And verify current credit score screen labels
        And click on one option on current credit score screen
        Then verify continue button is clicked
        And verify income screen labels
        And enter income in income screen
        Then verify continue button is clicked
        And verify how did you hear bright screen labels
        And click one option in how did you hear bright screen
        Then verify continue button is clicked
        And verify setup bright account screen labels
        And click on once every month option
        Then verify continue button is clicked
        And verify connect your bank screen labels
        And verify connect checking account
        Then close browser
        Given launch chrome browser
        When go to brightmoney website
        And login button is clicked
        And re-login same phone number 
        And click get started button
        And verify add OTP screen labels
        Then adding OTP in OTP screen
        And verify choose checking selection screen labels
        Then verify continue button is clicked
        And verify ssn screen labels
        And enter ssn in ssn screen
        Then verify continue button is clicked

    @CbFunnel
    Scenario: validate onboarding user in cb funnel
        #Till user is enrolled
        Given launch chrome browser
        When go to brightmoney website
        And login button is clicked
        And add phone number
        And click get started button
        And verify add OTP screen labels
        Then adding OTP in OTP screen
        And verify debt free journey screen labels
        Then verify continue button is clicked
        And verify crush your debt screen labels
        And verify click on info button
        And verify bright credit FAQ screen labels
        And verify got it button is clicked
        Then verify continue button is clicked
        And verify getting best offers screen labels
        And verify click on info button in getting best offers screen
        And verify how bright helps FAQ screen labels
        And verify got it button is clicked
        Then verify continue button is clicked
        And verify how bright builder works screen labels
        And verify click info button in how bright builder works screen
        And verify bright credit FAQ screen labels
        And verify got it button is clicked
        Then verify tell me more button is clicked
        And verify create additional payment history screen labels
        And verify click info button in create additional payment history screen
        And verify bright credit FAQ screen labels 
        And verify got it button is clicked
        Then verify continue button is clicked
        And verify approve bright builder screen labels
        And verify click info button in approve bright builder screen
        And verify bright credit FAQ screen labels 
        And verify got it button is clicked
        And verify check box is clicked
        Then verify continue button is clicked
        And verify set up bright builder screen labels
        And verify date is clicked
        Then verify continue button is clicked
        And verify monet screen labels
        And verify other plans button is clicked
        And verify limited time offer screen labels
        And verify select plan button is clicked
        Then verify continue button is clicked

   







