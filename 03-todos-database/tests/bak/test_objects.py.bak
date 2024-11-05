import pytest

# Create Python Object (elsewhere in the codebase)
class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

"""
# Test manual, no bueno
def test_person_initialization():
    p = Student('John', 'Doe', 'Computer Science', 3)
    assert p.first_name == 'John', 'First name should be John'
    assert p.last_name == 'Doe', 'Last name should be Doe'
    assert p.major == 'Computer Science'
    assert p.years == 3
"""

def test_person_initialization(default_employee):
    assert default_employee.first_name == 'John', 'First name should be John'
    assert default_employee.last_name == 'Doe', 'Last name should be Doe'
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 3

@pytest.fixture
def default_employee():
    return Student('John', 'Doe', 'Computer Science', 3)

