# Created by Gaurav at 18/10/2023
Feature: Verify Credit Card APIs
	# Test cases for all APIs for Credit Card


Scenario: Submit Application
		Given the payLoad required for "Submit"
		When PostAPI method is executed for "Submit"
		Then status code of response should be 200
		And response is having "eligibility" as "APPROVED"
		And row is created in subsequent tables with application_type as "CREDIT_CARD_SECURED_APPLICATION_V1"

# Scenario: Verify multiple buid
# 		Given the payLoad details with "<buids>" for "<Submit>"
# 		When PostAPI method is executed for Application Submit
# 		Then status code of response should be 200

Scenario: user profile
		Given get_user_profile with "+11399315565"
		Then response is "13908"

Scenario: Verify Submit API
		Given Eligible bright uid
		And the payload req for "Submit" application
		When Post API is sent
