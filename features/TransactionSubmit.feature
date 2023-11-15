Feature: Verify Payments API

Scenario: Submit payment

    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
    And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payLoad required for "Create" with eligible buid
    When PostAPI method is executed for "Create"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with account_state as "CREATED_IN_PROCESSOR"
    Then row is created in subsequent tables in DB "payments" with card_state as "DEPOSIT_IN_PROGRESS"
    #Need To Add Deposit API Steps
    Given the payLoad required for "Transactions" with eligible buid
    When PostAPI method is executed for "Transactions"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "REAL_TIME_OFFER"

Scenario: Verify submit API with wrong meta data
        Given the payLoad required for "Submit"
        When PostAPI method is executed with incorrect meta for "Submit"
        Then status code of response should be 400

Scenario: Verify submit API with wrong BUID
        Given the user have incorrect BUID
        And the payload required for "Submit"
        When PostAPI method is executed for "Submit"
        Then status code of response should be 400

Scenario: Verify submit API with empty transaction_type
        Given the user have eligible BUID
        And transaction_type is None in payLoad
        And the payLoad required for "Submit"
        When PostAPI method is executed for "Submit"
        Then status code of response should be 400

Scenario: Verify submit API with empty checking account
        Given the user have eligible BUID
        And checking_account_pid is None in payLoad
        And the payLoad required for "Submit"
        When PostAPI method is executed for "Submit"
        Then status code of response should be 400