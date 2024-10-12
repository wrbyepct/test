"""Test School component class behaviors."""

import pytest
from school.component import Class, FrenchStudent, USStudent


@pytest.mark.parametrize(
    argnames="std_id, first_name, last_name, expected_speak_str",
    argvalues=[
        (1, "Jack", "LaMar", "Je m'appelle Jack LaMar. Comment vas-tu?"),
        (2, "Black", "Maria", "Je m'appelle Black Maria. Comment vas-tu?"),
    ],
)
def test__frech_student__speak_correct(
    std_id,
    first_name,
    last_name,
    expected_speak_str,
):
    """Test FrechStudent instance .speak method return correct french string."""
    fr_std = FrenchStudent(std_id, first_name, last_name)
    speak_str = fr_std.speak()

    assert speak_str == expected_speak_str


@pytest.mark.parametrize(
    argnames="std_id, first_name, last_name, expected_speak_str",
    argvalues=[
        (1, "Jack", "LaMar", "Hello! I'm Jack LaMar. What's your name?"),
        (2, "Black", "Maria", "Hello! I'm Black Maria. What's your name?"),
    ],
)
def test__us_student__speak_correct(
    std_id,
    first_name,
    last_name,
    expected_speak_str,
):
    """Test FrechStudent instance .speak method return correct french string."""
    us_std = USStudent(std_id, first_name, last_name)
    speak_str = us_std.speak()

    assert speak_str == expected_speak_str


def test__class_roll_call_method__correct():
    """Test class return correct roll call dict."""
    fr_students = [
        FrenchStudent(
            std_id=i,
            first_name="i.First Name",
            last_name="i.Last Name",
        )
        for i in range(1, 11)
    ]
    fr_roll_call_dict = {std.id: std.speak() for std in fr_students}

    fr_class = Class(fr_students)

    assert fr_class.roll_call() == fr_roll_call_dict

    us_students = [
        USStudent(
            std_id=i,
            first_name="i.First Name",
            last_name="i.Last Name",
        )
        for i in range(1, 11)
    ]
    us_roll_call_dict = {std.id: std.speak() for std in us_students}

    us_class = Class(us_students)

    assert us_class.roll_call() == us_roll_call_dict
