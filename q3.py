def longest_token(file_path):
    """
    Returns a tuple of the longest token in the file and the line it appears on.

    >>> longest_token("song.txt")
    ('Merrily,', 3)
    """
    longest = ''
    line_number = 0
    max_length = 0

    with open(file_path, 'r') as file:
        for i, line in enumerate(file, 1):
            tokens = line.split()
            for token in tokens:
                if len(token) > max_length:
                    longest = token
                    max_length = len(token)
                    line_number = i

    return longest, line_number

# Test the function with the provided example
print(longest_token("song.txt"))  # Output should be ('Merrily,', 3)
