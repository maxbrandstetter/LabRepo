Feature: BDD What is Faster

  Scenario: Read From File
    Given the user is researching speeds
    When a file name is entered
    Then the cities, distances, and speeds will be read

  Scenario: Select Speed
    Given the user is researching speeds
    When an estimated speed is selected
    Then the user can see which would be faster

  Scenario: Select HD Size
    Given the user is researching speeds
    When a hard drive size is selected
    Then the user has more data

  Scenario: Is HD or Network Faster
    When the user enters information
    Then the user can see which would be faster

  Scenario: Difference in Time
    When the user enters information
    Then the user can see the time difference


