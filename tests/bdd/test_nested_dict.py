# coding=utf-8
"""A nested dict feature tests."""
# python
from functools import partial
import random

# pypi
from expects import (
    equal,
    expect,
    raise_error,
)
from pytest_bdd import (
    given,
    then,
    when,
)
import pytest_bdd

# for testing
from .fixtures import katamari

# software under test
from graeae.collections.nested_dict import NestedDict

# constants
scenario = partial(pytest_bdd.scenario, '../features/nested_dict.feature')

# ******************** construction ******************** #
@scenario('The nested dict is created')
def test_the_nested_dict_is_created():
    return


@given('a nested dict with attributes set')
@given('a nested dict')
def a_nested_dict_with_attributes_set(katamari):
    katamari.nested = NestedDict()
    return


@when('the attributes are checked')
def the_attributes_are_checked(katamari):
    katamari.actual = dict(
        separator=katamari.nested.separator,
        dictionary = katamari.nested.dictionary
    )
    katamari.expected = dict(separator="/", 
                             dictionary={})
    return


@then('they are the expected attributes')
def they_are_the_expected_attributes(katamari):
    for attribute, expected in katamari.expected.items():
        expect(katamari.actual[attribute]).to(equal(expected))
    return


# ******************** starter dictionary ******************** #


@scenario("A starter dictionary is passed in")
def test_starter_dictionary():
    return


@given("a starter dictionary passed to a nested dict")
def setup_starter_dictionary(katamari):
    katamari.starter = dict(
        a=5,
        b="2",
        c=3
    )
    katamari.nested = NestedDict(dictionary=katamari.starter)
    return


@when("a value from the starter dict is retrieved from the nested dict")
def get_value_from_nested(katamari):
    key = random.choice(list(katamari.starter.keys()))
    katamari.actual = katamari.starter[key]
    katamari.expected = katamari.nested[key]
    return


@then("it's the expected value")
def check_value(katamari):
    expect(katamari.actual).to(equal(katamari.expected))
    return

# ******************** get ******************** #


@scenario("A path is used")
def test_path():
    return
    
#  Given a nested dict

@when("a path to a value is used as a key to get a value")
def get_path_value(katamari):
    dictionary = dict(
        a={"b": {"c": {"d": 3}}}
    )
    katamari.nested.dictionary = dictionary
    katamari.expected = dictionary["a"]["b"]["c"]["d"]
    katamari.actual = katamari.nested["a/b/c/d"]
    return

#  Then it's the expected value

# ********** get sub-dict ********** #


@scenario("An incomplete path is used")
def test_incomplete_path():
    return


@given("a nested dict with nested dicts")
def setup_nested_dicts(katamari):
    dictionary = dict(
        a={"b": {"c": {"d": 3}}}
    )

    katamari.nested = NestedDict(dictionary=dictionary)
    return


@when("a partial path is used as a key to get a sub-dict")
def get_sub_dict(katamari):
    katamari.expected = katamari.nested.dictionary["a"]["b"]
    katamari.actual = katamari.nested["a/b"]
    return


@then("it has the expected values")
def check_values(katamari):
    for key, expected in katamari.expected.items():
        expect(katamari.actual[key]).to(equal(expected))
    return


# ********** get non-existent ********** #


@scenario("A non-existent path is retrieved")
def test_bad_path():
    return
          
#  Given a nested dict with nested dicts


@when("a non-existent path is retrieved")
def get_bad_path(katamari):
    def bad_call():
        katamari.nested["a/b/q"]

    katamari.bad_call = bad_call
    katamari.expected = KeyError
    return


@then("it raises an exception")
def check_exception(katamari):
    expect(katamari.bad_call).to(raise_error(katamari.expected))
    return

# ******************** set ******************** #


@scenario("A value is set")
def test_set_value():
    return

#  Given a nested dict


@when("a value is set with a path")
def set_value(katamari):
    katamari.path = "x j q p".split()
    katamari.expected = 5
    katamari.nested["x/j/q/p"] = katamari.expected    
    return


@then("the value is at the end of the path")
def check_value_at_path(katamari):
    actual = katamari.nested.dictionary
    for key in katamari.path:
        actual = actual[key]
    expect(actual).to(equal(katamari.expected))
    return
