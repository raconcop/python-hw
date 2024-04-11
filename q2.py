def travel(directions, start):
    """
    Returns the new position after following the given directions from the starting position.

    >>> travel("NW! ewnW", (1, 2))
    (-1, 4)
    """
    x, y = start
    for char in directions:
        char = char.upper()
        if char == 'N':
            y += 1
        elif char == 'S':
            y -= 1
        elif char == 'E':
            x += 1
        elif char == 'W':
            x -= 1
    return x, y

# Test the function with the provided example
print(travel("NW! ewnW", (1, 2)))  # Output should be (-1, 4)
