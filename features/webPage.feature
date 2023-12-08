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
        # And verify re-enter pin heading
        # And verify reentering pin
        # And verify name screen heading

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

    






