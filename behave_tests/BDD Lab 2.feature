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

  Scenario: Preset Speed Selection
    Given the user is researching speeds
    When a preset is entered
    Then preset values replace current values

  Scenario: Create New City
    Given the user is researching speeds
    When a new city is entered

  Scenario: Write City to File
    Given the user is researching speeds
    When a new city is entered
    Then write the data to a file

  Scenario: Create Route
    Given the user is researching speeds
    When a new route is entered
    Then return total distance

  Scenario: Startup City Selection
    Given the user is researching speeds
    When a starting city is entered
    Then store that city

  Scenario: Network Latency
    Given the user is researching speeds
    When an expected latency is entered
    Then needed values are changed

  Scenario: Hard Drive Speed
    Given the user is researching speeds
    When a hard drive size is entered
    Then get drive speed