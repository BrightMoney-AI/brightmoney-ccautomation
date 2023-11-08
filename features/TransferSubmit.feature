Feature: Verify Payments API

Scenario: Submit payment
		Given the user have eligible BUID
        And the payLoad required for "Submit"
		When PostAPI method is executed for "Submit"
		Then status code of response should be 200
		And response is having "paymeny_type" as "REAL_TIME_OFFER"
        And response is having "payment_state" as ""
		And row is created in subsequent tables in DB "payments"

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