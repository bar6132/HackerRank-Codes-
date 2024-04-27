def plus_one(digits):
    carry = 1

    for i in reversed(range(len(digits))):
        total = digits[i] + carry
        digits[i] = total % 10
        carry = total // 10

        if carry == 0:
            break

    if carry != 0:
        digits.insert(0, carry)

    return digits


print(plus_one([1, 2, 3]))  # Output: [1,2,4]
print(plus_one([4, 3, 2, 1]))  # Output: [4,3,2,2]
print(plus_one([9]))  # Output: [1,0]
