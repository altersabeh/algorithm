Feature: Creating valid plane figures

  Scenario: Creating a circle with a specific radius
    Given a circle radius of 5.5
    When the circle is created
    Then the circle's radius should be 5.5

  Scenario: Creating a rectangle with specific dimensions
    Given a rectangle width of 10.0
    And a rectangle height of 5.0
    When the rectangle is created
    Then the rectangle's width should be 10.0
    And the rectangle's height should be 5.0

  Scenario: Creating a square with a specific side length
    Given a square side length of 4.0
    When the square is created
    Then the square's side length should be 4.0
