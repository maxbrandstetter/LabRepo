Feature: BDD What is Faster

  Scenario: Read From File
    Given the user is researching speeds
    When a file name is entered
    Then the cities, distances, and speeds will be read

  Scenario: Select Speed
    Given the user is researching speeds
    When an estimated speed is entered

  Scenario: Select HD Size
    Given the user is researching speeds
    When a hard drive size is entered

  Scenario: Is HD or Network Faster
    Given the user is researching speeds
    When an estimated speed is entered
    When a hard drive size is entered
    When a city is entered
    Then the user can see which would be faster

  Scenario: Difference in Time
    Given the user is researching speeds
    When an estimated speed is entered
    When a hard drive size is entered
    When a city is entered
    Then the user can see the time difference
