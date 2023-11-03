
Feature: Verify Submit Application API

@submitApiOne
Scenario: Verify Submit API
		Given User have eligible bright uid
		And the payLoad required for "Submit" with eligible buid
		When PostAPI method is executed for "Submit"
		Then status code of response should be 200
		And response is having "application_state" as "UNDERWRITING_IN_PROGRESS"
		And row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"


@submitApi
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


Scenario: Verify Submit API with Large Income Value
	Given User have eligible bright uid
	And the payload req for "Submit" application with a large income value
	When PostAPI method is executed for "Submit"
	Then the response status code should be 200


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


Scenario: Verify Submit API with Large Income Value and Complete Data
	Given User have eligible bright uid
	And the payload req for "Submit" application with a large income value and complete data
	When PostAPI method is executed for "Submit"
	Then the response status code should be 200
	And response is having "application_state" as "UNDERWRITING_IN_PROGRESS"
	And row is created in subsequent tables in DB "payments" with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"

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
	

