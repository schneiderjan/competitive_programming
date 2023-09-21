def expected_rounds(n, probabilities):
    dp = [0.0] * (1 << n)
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                continue  # Child i is already eliminated in this state
            dp[mask] += probabilities[i] * dp[mask ^ (1 << i)] / (1 - probabilities[i])
    return dp[(1 << n) - 1]

# Input
# n = int(input())
# probabilities = [float(input()) for _ in range(n)]

# Calculate and print the expected number of rounds
n = 3
probabilities = [0.5 ,0.5,0.5]
expected_rounds_value = expected_rounds(n, probabilities)
print(expected_rounds_value)