
# Created by Gaurav at 18/10/2023
Feature: validate usm api
	# Test cases for all APIs for Credit Card


Scenario: validate sign in API success
	Given payload required for signin API
	When postAPI method is executed
	Then validate response code should be 200
	And access or refresh token or bright_uid is not null
	And action name is correct

Scenario: validate sign in API failure
	Given negative payload for signin API
	When postAPI method is executed
	Then validate respone code should be 400
	And response contain event_name field

Scenario: validate app pin enable API
	Given previous API is hit in sequence
	And payload for app pin enabel
	When app pin enable is hit
	Then validate response code should be 200
	And validate action name and pii data type

