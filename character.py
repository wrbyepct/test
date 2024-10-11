"""Charcter global settings."""

import random

DEFAULT_MALE_STR = """

:)

"""


class AttackMixins:
    """Character attacks Mixins."""

    strength: int
    intelligence: int

    def slash(self) -> int:
        """
        Return calculated slash damage according to character's strength.

        Returns:
            int: slash damage

        """
        return self.strength * 10

    def iceball(self) -> int:
        """Return slash damage according to character's intelligence."""
        return self.intelligence * 19


class Character(AttackMixins):
    """Character instance."""

    def __init__(self, character_str: str) -> None:
        self.presenting_str = character_str

        self.strength = self.__set_strength()
        """Character's strength value."""

        self.intelligence = self.__set_intelligence()
        """Character's intelligence value."""

    def __set_strength(self) -> int:
        # """Generate character strength random value."""
        return random.randint(1, 11)

    def __set_intelligence(self) -> int:
        return random.randint(1, 11)


def get_character(character_str: str = DEFAULT_MALE_STR) -> Character:
    """Get character instance."""
    return Character(character_str)
