#!/usr/bin/python3
"""
Minimum Operations Module
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in a file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations to achieve n H characters.
             Returns 0 if it is impossible to achieve n H characters.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:  # Check if factor is a divisor of n
            operations += factor  # Add the factor to operations
            n //= factor  # Reduce n by the factor
        else:
            factor += 1  # Move to the next potential factor

    return (operations)
