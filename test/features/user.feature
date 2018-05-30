Feature: Testing out behave on flask

  Scenario: This is how I'm testing whether I can get behave to work on Flask
    Given The flask application is running
    Then I should receive a 200 response
    And The user should see Hello, World