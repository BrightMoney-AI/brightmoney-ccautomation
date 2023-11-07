
Feature: Verify Activate Card API

Scenario: Verify Activate API
        Given User have eligible bright uid
        And the payLoad required for "Submit" with eligible buid
        When PostAPI method is executed for "Submit"
        Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
		Given the payLoad required for "Poll" with eligible buid
		When PostAPI method is executed for "Poll" 
        Then status code of response should be 200
        And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
        Given the payLoad required for "Create" with eligible buid
        When PostAPI method is executed for "Create"
        
        Then status code of response should be 200