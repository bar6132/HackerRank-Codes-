def climbStairs(n):
    if n <= 2:
        return n
    prev1, prev2 = 1, 2
    for _ in range(n - 2):
        prev1, prev2 = prev2, prev1 + prev2

    return prev2


print(climbStairs(2))
print(climbStairs(4))
print(climbStairs(5))
print(climbStairs(10))
