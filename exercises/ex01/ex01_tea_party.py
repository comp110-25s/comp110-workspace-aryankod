"""A Tea Party Cost Calculator"""

__author__ = "730653702"


def main_planner(guests: int) -> None:
    """Entrypoint of the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=(treats(people=guests)))
        )
    )


def tea_bags(people: int) -> int:
    """Return the number of tea bags needed at the party."""
    return people * 2


def treats(people: int) -> int:
    """Return the number of treats needed at the party."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Return the cost of the party"""
    return float(tea_count * 0.5) + float(treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
