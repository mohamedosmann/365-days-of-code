from bisect import bisect_right

def find_last_non_conflicting(missions, index):
    """Binary search to find the last mission that does not overlap with the current one."""
    left, right = 0, index - 1
    while left <= right:
        mid = (left + right) // 2
        if missions[mid][1] <= missions[index][0]:  # Non-overlapping
            if missions[mid + 1][1] <= missions[index][0]:
                left = mid + 1
            else:
                return mid
        else:
            right = mid - 1
    return -1

def max_mission_profit(missions):
    """Computes the maximum profit by scheduling non-overlapping missions."""
    # Sort missions by their end time
    missions.sort(key=lambda x: x[1])

    # DP table to store max profit at each step
    n = len(missions)
    dp = [0] * n
    dp[0] = missions[0][2]  # First mission's profit

    for i in range(1, n):
        # Include current mission
        include_profit = missions[i][2]
        last = find_last_non_conflicting(missions, i)
        if last != -1:
            include_profit += dp[last]

        # Exclude current mission (take previous max profit)
        dp[i] = max(include_profit, dp[i - 1])

    return dp[-1]  # Maximum profit

# 🚀 Example Test Case
missions = [
    (1, 3, 50),  
    (2, 5, 20),  
    (4, 6, 70),  
    (6, 7, 30)   
]

print("Max Profit:", max_mission_profit(missions))
