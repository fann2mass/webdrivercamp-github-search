Feature: GitHub User Search

  Background:
     Given Browser: Navigate to https://gh-users-search.netlify.app/

  Scenario Outline: verify number of followers against API
    When UI: search for "<username>"
    And API: send GET request "/users/<username>/followers?per_page=100"
    And API: verify status code is "200"
    Then UI: verify total number of Followers
    Examples:
      | username  |
      | jenisys   |
      | fann2mass |

  Scenario Outline: verify number of following against API
    When UI: search for "<username>"
    And API: send GET request "/users/<username>"
    And API: verify status code is "200"
    Then UI: verify total number of Following
    Examples:
      | username  |
      | jenisys   |
      | fann2mass |

  Scenario Outline: verify number of Gists against API
    When UI: search for "<username>"
    And API: send GET request "/users/<username>"
    And API: verify status code is "200"
    Then UI: verify total number of Gists
    Examples:
      | username  |
      | jenisys   |
      | fann2mass |

  Scenario Outline: verify total number of Repos against API
    When UI: search for "<username>"
    And API: send GET request "/users/<username>/repos?per_page=1000"
    And API: verify status code is "200"
    Then UI: verify total number of Repos
    Examples:
      | username  |
      | jenisys   |
      | fann2mass |

  Scenario Outline: verify user info after search
    When UI: search for "<username>"
    And API: send GET request "/users/<username>"
    And API: verify status code is "200"
    Then UI: verify user info
    Examples:
      | username  |
      | fann2mass |
      | 1st1      |

  Scenario Outline: verify blog link redirects to corresponding url
    When UI: search for "<username>"
    And API: send GET request "/users/<username>"
    And API: verify status code is "200"
    And UI: click on blog link
    Then Browser: verify blog url
    Examples:
      | username  |
      | 1st1      |

  Scenario Outline: verify follow button redirects to corresponding github url
    When UI: search for "<username>"
    And API: send GET request "/users/<username>"
    And API: verify status code is "200"
    And UI: click on follow button
    Then Browser: verify github url
    Examples:
      | username  |
      | 1st1      |

  Scenario Outline: verify user search can be performed after clicking enter/return
    When UI: search for "<username>" using enter/return
    And API: send GET request "/users/<username>"
    And API: verify status code is "200"
    Then UI: verify user info
    Examples:
      | username  |
      | 1st1      |

  Scenario Outline: verify user search with incorrect username
    When UI: search for "<username>" using enter/return
    And API: send GET request "/users/<username>"
    And API: verify status code is "404"
    Then UI: verify followers, following, repos and gists is zero
    And UI: verify Followers list is empty
    And UI: verify user data is empty
    Examples:
      | username                    |
      | incorrectUserName1234asdada |

  Scenario Outline: verify correct number of followers is displayed in the followers list
    When UI: search for "<username>"
    And API: send GET request "/users/<username>/followers?per_page=100"
    And API: verify status code is "200"
    Then UI: verify correct number of Followers is displayed in the followers list
    Examples:
      | username  |
      | jenisys   |

  Scenario Outline: verify number of followers is 100 if account has more than 100 followers
    When UI: search for "<username>"
    And API: send GET request "/users/<username>/followers?per_page=100"
    And API: verify status code is "200"
    Then UI: verify number of Followers is 100 in the list
    Examples:
      | username |
      | 1st1     |
