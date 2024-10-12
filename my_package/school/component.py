"""Some doc."""

# ruff: noqa: D102, T201
from __future__ import annotations

from typing import Generic, Protocol, TypeVar

TStudent = TypeVar("TStudent", bound="Student")


class Student(Protocol):
    """Student class."""

    id: int

    def speak(self) -> str:
        """To be implemented by subclass of Student."""
        ...


class FrenchStudent:
    """French Student."""

    def __init__(self, std_id: int, first_name: str, last_name: str) -> None:
        self.id = std_id
        self.first_name = first_name
        self.last_name = last_name

    def speak(self) -> str:
        """Return french greeting."""
        return f"Je m'appelle {self.first_name} {self.last_name}. Comment vas-tu?"


class USStudent:
    """US Student."""

    def __init__(self, std_id: int, first_name: str, last_name: str) -> None:
        self.id = std_id
        self.first_name = first_name
        self.last_name = last_name

    def speak(self) -> str:
        """Return English greeting."""
        return f"Hello! I'm {self.first_name} {self.last_name}. What's your name?"

    def play(self) -> str:
        return "US students play!"


class Class(Generic[TStudent]):
    """School class."""

    def __init__(self, students: list[TStudent]) -> None:
        self.students = students

    def roll_call(self) -> dict:
        """Roll call student's id and call '.speak()'."""
        return {std.id: std.speak() for std in self.students}
