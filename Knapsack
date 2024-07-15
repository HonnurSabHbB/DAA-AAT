def unboundedKnapsack(k, arr):
    # Create a DP array to store maximum sum for each value up to k
    dp = [0] * (k + 1)

    # Iterate through each possible value from 1 to k
    for i in range(1, k + 1):
        for num in arr:
            if num <= i:
                dp[i] = max(dp[i], dp[i - num] + num)
    
    # The value at dp[k] will be the maximum sum not exceeding k
    return dp[k]

# Input reading part
import sys
input = sys.stdin.read
data = input().split()

# Read the number of test cases
t = int(data[0])
index = 1

results = []

for _ in range(t):
    # Read n and k
    n = int(data[index])
    k = int(data[index + 1])
    index += 2
    
    # Read the array
    arr = list(map(int, data[index:index + n]))
    index += n
    
    # Calculate the result for this test case
    result = unboundedKnapsack(k, arr)
    results.append(result)


for res in results:
    print(res)
