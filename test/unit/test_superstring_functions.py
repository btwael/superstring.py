from pytest import fixture

from superstring import SuperString


@fixture
def super_string():
    return SuperString("test")


def test_length(super_string):
    assert super_string.length() == 4
    assert len(super_string) == super_string.length()


def test_character_at(super_string):
    assert super_string.characterAt(0) == "t"
    assert super_string[0] == "t"
