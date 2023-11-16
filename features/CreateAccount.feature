Feature: Verify Create Account Poll API


Scenario: Verify Create API
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

@negative
Scenario: Verify Create API with empty pid
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
Scenario: Verify Create API with empty auth signal
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
Scenario: Verify Create API with empty bright uid 
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
Scenario: Verify Create API with empty meta 
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