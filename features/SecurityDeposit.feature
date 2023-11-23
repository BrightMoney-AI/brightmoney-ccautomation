Feature: Verify Security Deposit API


Scenario: Verify Security Deposit Payment
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
    Given the payLoad required for "Deposit" with eligible buid
    When PostAPI method is executed for "Deposit"


@negative
Scenario: Verify Security Deposit Payment with Missing Account PID Field
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
    And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payload req with empty pid with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400

@negative
Scenario: Verify Security Deposit Payment with Invalid Transaction Type
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
    And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payload req with empty auth signal with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400 

@negative
Scenario: Verify Security Deposit Payment with Insufficient Amount for Security Deposit 
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
    And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payload req with empty bright uid with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400

@negative
Scenario: Verify Security Deposit Payment with Payment Review in Progress
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
    And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payload req with empty meta data with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400 


@negative
Scenario: Verify Security Deposit Payment with Failure Feedback from Payment System
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
    And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payload req with empty meta data with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400  




@negative
Scenario: Verify Security Deposit Payment with Invalid Account PID Format
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
    And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payload req with empty meta data with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400                  



@negative
Scenario: Verify Security Deposit Payment with Missing Pull Account PID Field
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
    And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payload req with empty meta data with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400                  