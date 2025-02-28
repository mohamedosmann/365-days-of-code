def spaceX_cargo_optimization(cargo, capacity):
    n = len(cargo)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        weight, value = cargo[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], value + dp[i-1][w - weight])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Find the selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(cargo[i-1])
            w -= cargo[i-1][0]

    return dp[n][capacity], selected

# Example Test
cargo = [(2, 30), (3, 50), (4, 70), (5, 80)]
capacity = 5

max_value, selected_cargo = spaceX_cargo_optimization(cargo, capacity)
print("Maximum Cargo Value:", max_value)
print("Selected Cargo:", selected_cargo)
