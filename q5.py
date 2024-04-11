def most_frequent(nums):
    """
    Returns the integer value that appears most frequently in the list.

    >>> most_frequent([1, 2, 1, 2, 1])
    1
    >>> most_frequent([0])
    0
    >>> most_frequent([-1, 2, 2])
    2
    >>> most_frequent([1, 2, 1, 1, 2, 3, 2, 2, 3, 1])
    1
    """
    count_dict = {}
    
    # Count the occurrences of each number in the list
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Find the number with the maximum count
    max_count = max(count_dict.values())
    
    # Find the number(s) with the maximum count
    most_frequent_nums = [key for key, value in count_dict.items() if value == max_count]
    
    # Return the first most frequent number
    return most_frequent_nums[0]

