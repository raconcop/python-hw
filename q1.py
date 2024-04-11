def is_relatively_prime(n, m):
    """
    Returns True if n and m are relatively prime, False otherwise.

    >>> is_relatively_prime(12, 13)
    True
    >>> is_relatively_prime(12, 14)
    False
    >>> is_relatively_prime(5, 9)
    True
    >>> is_relatively_prime(8, 9)
    True
    >>> is_relatively_prime(8, 1)
    True
    """
    if n < 1 or m < 1:
        raise ValueError("Both numbers should be at least 1.")
    
    # 1 is relatively prime with every number
    if n == 1 or m == 1:
        return True
    
    # Find the smaller number between n and m
    smaller = min(n, m)
    
    # Check if there is any common factor other than 1
    for i in range(2, smaller + 1):
        if n % i == 0 and m % i == 0:
            return False
    
    return True
