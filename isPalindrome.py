def is_palindrome(x):
    if x < 0:
        return False
    rev = 0
    temp = x
    while temp > 0:
        dig = temp % 10
        rev = rev * 10 + dig
        temp = temp // 10
    return x == rev


print(is_palindrome(12121))  # True
print(is_palindrome(313))  # True
print(is_palindrome(122))  # False
