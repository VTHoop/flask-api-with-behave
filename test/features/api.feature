Feature: Test out each scenario of a RESTful API

  Scenario: This will ensure that a bike object get request provides a successful response
    Given a service pings bike service GET URI without an ID
    Then I should receive a 200 response

  Scenario: If a bad ID is given on a single bike request, 404 will be returned
    Given a service pings the bike service GET URI for a bad bike ID
    Then I should receive a 404 response