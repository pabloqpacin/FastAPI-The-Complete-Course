##### UNIT TESTING #####
### Assertion Test ###

# Validate Integers
def test_equal_or_not_equal():
    assert 3 == (2+1)
    assert 3 != (2+2)

# Validate Instances
def test_is_instance():
    assert isinstance('this is a string', str)
    assert not isinstance('10', int)
    assert isinstance(10, int)

# Validate Booleans
def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False

# Validate Types
def test_type():
    assert type('Hello' == str)
    assert type('World' != int)

# Validate Greater & Less Than
def test_greater_and_less_than():
    assert 7 > 3
    assert 4 < 10

# Validate Types
def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)

"""
The all() function returns True if all elements in the list are "truthy" (not False, 0, None, or an empty value).
In num_list, all values are non-zero integers, so they are all considered truthy.
Therefore, all(num_list) evaluates to True, and this assertion passes.

The any() function returns True if any element in the list is truthy.
any_list only contains False values, so any(any_list) evaluates to False.
The assertion not any(any_list) checks that no elements in any_list are truthy (in other words, all are False), which is True, so this assertion passes.
"""

