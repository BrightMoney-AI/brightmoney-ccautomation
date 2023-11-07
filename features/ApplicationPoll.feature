Feature: Verify Application Poll API

@pollone
Scenario: Verify Poll API
		Given User have eligible bright uid
        And the payLoad required for "Submit" with eligible buid
        When PostAPI method is executed for "Submit"
		Given the payLoad required for "Poll" with eligible buid
		When PostAPI method is executed for "Poll" 
        Then status code of response should be 200
        And row is created in subsequent tables in DB "payments" with application_state as "WAITING_ON_USER_RESPONSE_ON_AGREEMENT"



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
               
		