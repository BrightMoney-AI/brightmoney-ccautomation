
Feature: Verify Create Account Poll API
@create
Scenario: Verify Create API
		Given User have eligible bright uid
        And the payLoad required for "Submit" with eligible buid
        When PostAPI method is executed for "Submit"
		Given the payLoad required for "Poll" with eligible buid
		When PostAPI method is executed for "Poll"
        Given the payLoad required for "Create" with eligible buid
        When PostAPI method is executed for "Create"
        Then status code of response should be 200



       