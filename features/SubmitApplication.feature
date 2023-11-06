# Created by Gaurav at 18/10/2023
Feature: Verify Credit Card APIs
	# Test cases for all APIs for Credit Card

@smoke
Scenario: Submit Application
		Given the payLoad required for "Submit"
		When PostAPI method is executed for "Submit"
		Then status code of response should be 200
		And response is having "eligibility" as "REAL_TIME_OFFER"
		And row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"

@regression
Scenario: Verify Submit API
		Given User have eligible bright uid
		And the payLoad required for "Submit" with eligible buid
		When PostAPI method is executed for "Submit"
		Then status code of response should be 200
		And response is having "application_state" as "UNDERWRITING_IN_PROGRESS"
		And row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"


@regression
Scenario: Verify Submit API with dynamic data
		Given User have eligible bright uid
		And the payLoad required for "Submit" with eligible buid
		When PostAPI method is executed for "Submit" with dynamic data
		Then status code of response should be 200
		And response is having "application_state" as "UNDERWRITING_IN_PROGRESS"
		And row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"