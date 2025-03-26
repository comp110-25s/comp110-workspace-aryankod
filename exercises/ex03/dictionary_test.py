""""Testing the Fourth Exercise. Units tests for dictionary.py functions."""

__author__ = "730653702"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


def test_invert_basic():
    """Tests basic key-value inversion"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_key_error():
    """Tests for KeyError with duplicate values."""
    with pytest.raises(KeyError):
        invert({"bill": "belichick", "steve": "belichick"})


def test_invert_pair():
    """Tests inverting only one pair."""
    assert invert({"ketchup": "mustard"}) == {"mustard": "ketchup"}


def test_count_basic():
    """Tests basic counting."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_unique():
    """Tests counting unique items."""
    assert count(["x", "y", "z"]) == {"x": 1, "y": 1, "z": 1}


def test_count_empty():
    "Tests counting an empty list."
    assert count([]) == {}


def test_favorite_color_basic():
    """Tests basic example where blue obviously wins."""
    assert favorite_color({"Bob": "blue", "Bill": "blue", "Joe": "red"}) == "blue"


def test_favorite_color_tie():
    """Tests if tie-breaking by first occurence wins."""
    assert (
        favorite_color({"Bob": "blue", "Bill": "blue", "Joe": "red", "John": "red"})
        == "blue"
    )


def test_favorite_color_single():
    """Test for when there's only one color."""
    assert favorite_color({"Bob": "blue"}) == "blue"


def test_bin_len_basic():
    """Tests binning easy words by length"""
    assert bin_len(["cat", "dog", "fish"]) == {3: {"cat", "dog"}, 4: {"fish"}}


def test_bin_len_empty():
    """Tests binning an empty list."""
    assert bin_len([]) == {}


def test_bin_len_double():
    "Tests binning with double words"
    assert bin_len(["cat", "fish", "cat", "apple"]) == {
        3: {"cat"},
        4: {"fish"},
        5: {"apple"},
    }
