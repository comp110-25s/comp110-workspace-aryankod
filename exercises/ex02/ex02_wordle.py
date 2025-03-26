""""A Python equivalent of Wordle."""

__author__ = "730653702"


def contains_char(search_string: str, character: str) -> bool:
    """Checks if a character is in the string by iteration."""
    assert len(character) == 1, f"len('{character}') is not 1"

    counter = 0
    while counter < len(search_string):
        if search_string[counter] == character:
            return True
        counter += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns emoji string quantifying guess accuracy."""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    counter = 0
    emoji_result = ""

    while counter < len(guess):
        if guess[counter] == secret[counter]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[counter]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        counter += 1

    return emoji_result


def input_guess(expected_length: int) -> str:
    """Verifies the user's guess length"""

    user_guess = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main(secret: str) -> None:
    """The entrypoint of the program and the main game loop."""

    turns = 1
    max_turns = 6
    won = 0
    secret_length = len(secret)

    while turns <= max_turns and won == 0:
        print(f"=== Turn {turns}/{max_turns} ===")
        attempt = input_guess(secret_length)
        result = emojified(attempt, secret)
        print(result)

        if attempt == secret:
            won += 1
        else:
            turns += 1

    if won == 1:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
