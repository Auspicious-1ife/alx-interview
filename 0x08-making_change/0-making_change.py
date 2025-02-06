def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total
    :param coins: List of available coin denominations
    :param total: The target amount
    :return: Minimum number of coins needed to make the total, or -1 if not possible
    """
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    
    for coin in coins:
        if total == 0:
            break
        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin
    
    return count if total == 0 else -1

