Feature: Verify All Negative Test Cases

Scenario: Verify Submit API
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    And response is having "application_state" as "UNDERWRITING_IN_PROGRESS"
    And row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"

Scenario: Verify Submit API with wrong type
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    And response is having "application_state" as "UNDERWRITING_IN_PROGRESS"
    #add error msg 
    And row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V2"    

Scenario: Verify Submit API with Missing Required Field
	Given User have eligible bright uid
	And the payload req for "Submit" with a missing required field
	When PostAPI method is executed for "Submit"
	Then the response status code should be 400

#check with dev
Scenario: Verify Submit API with  Missing Loan Version
	Given User have eligible bright uid
	And the payload req for "Submit" application with an Missing loan version
	When PostAPI method is executed for "Submit"
	Then the response status code should be 400

#check with dev/gaurav sir
Scenario: Verify Submit API with Missing Meta Information
	Given User have eligible bright uid
	And the payload req for "Submit" application with missing meta information
	When PostAPI method is executed for "Submit"
	Then the response status code should be 400

Scenario: Verify Submit API with Missing Application Data
	Given User have eligible bright uid
	And the payload req for "Submit" application with missing application data
	When PostAPI method is executed for "Submit"
	Then the response status code should be 400

Scenario: Verify Submit API with Null Values
	Given User have eligible bright uid
	And the payload req for "Submit" application with null values
	When PostAPI method is executed for "Submit"
	Then the response status code should be 400

#check with dev 
Scenario: Verify Submit API with Empty Auth Signals
    Given User have eligible bright uid
    And the payload req for "Submit" application with empty auth signals
    When PostAPI method is executed for "Submit"
    Then the response status code should be 400

#Check with dev
Scenario: Verify Submit API with Invalid Product
    Given User have eligible bright uid
    And the payload req for "Submit" application with an invalid product
    When PostAPI method is executed for "Submit"
    Then the response status code should be 400

Scenario: Verify Submit API with Missing Income Information
    Given User have eligible bright uid
    And the payload req for "Submit" application with missing income information
    When PostAPI method is executed for "Submit"
    Then the response status code should be 400

Scenario: Verify Submit API with Null Loan Version
    Given User have eligible bright uid
    And the payload req for "Submit" application with null loan version
    When PostAPI method is executed for "Submit"
    Then the response status code should be 400

Scenario: Verify Poll API With Wrong Application ID
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Given the payload req for "Poll" with wrong application id
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 400
    
Scenario: Verify Poll API With NULL Application ID
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Given the payload req for "Poll" with null application id
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 400

Scenario: Verify Poll API With Empty Meta Data
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Given the payload req for "Poll" with empty meta data
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 400

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


Scenario: Verify Create API with empty pid with wrong state
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
     #add error msg 
    And row is created in subsequent tables in DB "payments" with application_state as "UNKNOWN"
    Given the payload req with empty pid with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400


Scenario: Verify Create API with empty pid with wrong app type
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
     #add error msg 
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
    And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payload req with empty pid with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400


Scenario: Verify Create API with empty pid with wrong state another
    Given User have eligible bright uid
    And the payLoad required for "Submit" with eligible buid
    When PostAPI method is executed for "Submit"
    Then status code of response should be 200
     #add error msg 
    Then row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_V1"
    Given the payLoad required for "Poll" with eligible buid
    When PostAPI method is executed for "Poll" 
    Then status code of response should be 200
     #add error msg 
    And row is created in subsequent tables in DB "payments" with application_state as "ON_USER_RESPONSE_ON_AGREEMENT"
    Given the payload req with empty pid with rest same
    When PostAPI method is executed for "Create"
    Then status code of response should be 400    

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

