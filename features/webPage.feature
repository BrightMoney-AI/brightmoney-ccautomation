Feature: Bright Money web screen

    Scenario: Check first screen after loading the URL
        Given launch Chrome browser
        When go to brightmoney website
        Then verify text present on the page
        And close browser


