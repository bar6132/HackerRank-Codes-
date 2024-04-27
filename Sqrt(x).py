def mysqrt(x):
    if x < 2:
        return x
    left, right = 2, x // 2
    while left <= right:
        mid = (left + right) // 2
        sqrt = mid * mid
        if sqrt == x:
            return mid
        elif sqrt < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


print(mysqrt(4))  # Output: 2
print(mysqrt(8))  # Output: 2
print(mysqrt(16))  # Output: 4
print(mysqrt(1000000000))  # Output: 10000

