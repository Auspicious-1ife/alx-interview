#!/usr/bin/python3
"""
Module for solving the minimum coin change problem.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of available coins (positive integers).
        total (int): The target amount to be reached.

    Returns:
        int: The minimum number of coins needed to reach total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met with the given coins.
    """
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0  # Counter for the number of coins used
    
    for coin in coins:
        if total == 0:
            break
        num_coins = total // coin  # Max coins of this denomination that can be used
        count += num_coins
        total -= num_coins * coin
    
    return count if total == 0 else -1

