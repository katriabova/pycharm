import pytest

from src.generators import card_number_generator


def test_card_number_generator():
    gen = card_number_generator(1, 2)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
