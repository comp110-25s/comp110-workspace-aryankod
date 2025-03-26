"""Empty Docstring for fun"""


def celsius_to_fahrenheit(degrees: int) -> float:
    """Convert degrees Celsius to degrees Fahrenheit"""
    return (degrees * 9 / 5) + 32


print(celsius_to_fahrenheit(degrees=0))

print(celsius_to_fahrenheit(degrees=10))


def what_he_smell_like(name: str) -> str:
    """For Haiden"""
    if name[0] == "H" or name[0] == "h":
        return name + " smells smegilicous!"
    elif name[0] == "A" or name[0] == "a":
        return name + " smells like cheese!"
    else:
        return name + " smells like a normal person."


def perimeter(length: float, width: float) -> float:
    """Calculate a rectangle's perimeter"""
    return 2 * (width + length)
