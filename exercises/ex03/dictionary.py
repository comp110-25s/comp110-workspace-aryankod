""""The Fourth Exercise."""

__author__ = "730653702"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in a dictionary."""
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            raise KeyError(
                "There is a duplicate that exists! You cannot invert this dictionary."
            )
        inverted[value] = key
    return inverted


def count(list_in_use: list[str]) -> dict[str, int]:
    """Counts how often each string is in a list."""
    counter = {}
    for item in list_in_use:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most common favorite color."""
    color_counts = count(list(colors.values()))
    max_color = ""
    max_count_value = -1
    for i in colors.values():
        if int(color_counts[i]) > max_count_value:
            max_color = i
            max_count_value = color_counts[i]
    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins words by length into a dictionary."""
    bins = {}
    for word in words:
        if len(word) not in bins:
            bins[len(word)] = {word}
        else:
            if word not in bins[len(word)]:
                bins[len(word)].add(word)
    return bins
