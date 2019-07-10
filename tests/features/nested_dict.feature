Feature: A nested dict

Scenario: The nested dict is created
  Given a nested dict with attributes set
  When the attributes are checked
  Then they are the expected attributes

Scenario: A starter dictionary is passed in
  Given a starter dictionary passed to a nested dict
  When a value from the starter dict is retrieved from the nested dict
  Then it's the expected value

Scenario: A path is used
  Given a nested dict
  When a path to a value is used as a key to get a value
  Then it's the expected value

Scenario: An incomplete path is used
  Given a nested dict with nested dicts
  When a partial path is used as a key to get a sub-dict
  Then it has the expected values

Scenario: A non-existent path is retrieved
  Given a nested dict with nested dicts
  When a non-existent path is retrieved
  Then it raises an exception


Scenario: A value is set
  Given a nested dict
  When a value is set with a path
  Then the value is at the end of the path
