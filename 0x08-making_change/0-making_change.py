#!/usr/bin/python3
"""the fewest number of coins needed to meet a given amount total."""


def makeChange(coins, total):
    """
    function that returns the total coins needed for a change
    best senero
    """
    if total <= 0:
        return 0

    # Initialize DP table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    # Fill DP table
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is infinity, total can't be made
    return dp[total] if dp[total] != float('inf') else -1
