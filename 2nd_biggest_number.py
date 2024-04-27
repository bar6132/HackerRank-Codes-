lst = [441]

def get_sec(lst: list):
    largest = lst[0]
    if len(lst) <= 1:
        return lst[0]
    elif len(lst) <= 2:
        sec_largest = lst[1]
        if largest > sec_largest:
            return sec_largest
        elif sec_largest > largest:
            return largest
    if len(lst) <= 3:
        largest = lst[0]
        sec_largest = lst[1]
        for item in lst:
            if item > largest:
                sec_largest = largest
                largest = item
            elif sec_largest < item < largest:
                sec_largest = item

        return sec_largest


print(get_sec(lst))
import time


def arrange_items(items: list):
    arranged_items = []

    for item in items:
        if item == 'white':
            arranged_items.append(item)

    for item in items:
        if item == 'red':
            arranged_items.append(item)

    for item in items:
        if item == 'black':
            arranged_items.append(item)

    return print(arranged_items)


items = ['black', 'white', 'black','red', 'black', 'white', 'black','red', 'red', 'red', ]
arrange_items(items)





def arrange_items(items: list):
    arranged_items = []
    colors = ['white', 'red', 'black']

    for color in colors:
        arranged_items.extend([item for item in items if item == color])

    return print(arranged_items)

def arrange_items(items: list):
    count_white = items.count('white')
    count_red = items.count('red')
    count_black = items.count('black')

    items.clear()

    items.extend(['white'] * count_white)
    items.extend(['red'] * count_red)
    items.extend(['black'] * count_black)
    print(items)

items = ['black', 'white', 'black', 'red', 'black', 'white', 'black', 'red', 'red', 'red']

arrange_items(items)



# create a function that takes a string and returns the most common character in the string
def most_common_str():
    string = input("input a string: ")
    return max(set(string), key=string.count)

print(most_common_str())

def most_common_char(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            print(char_count)
            char_count[char] += 1
            print(char_count)
        else:
            print(char_count)
            char_count[char] = 1
            print(char_count)
    most_common = None
    max_count = 0

    for char, count in char_count.items():
        if count > max_count:

            most_common = char
            max_count = count

    return most_common


# input_str = "my1 ma1ne i1s m1ary1"
input_str = input('Enter you words/sentence : ')
result = most_common_char(input_str)
print("The most common character is:", result)


def sor(lst):
    print(lst)
    print(list(reversed(lst)))

lst = [1, 2, 3, 4]

sor(lst)


def print_unique_char(string):
    char_count = {}

    for char in string:
        char_count[char] = char_count.get(char, 0) + 1


    for char in string:
        if char_count[char] == 1:
            print(char)
            return

    print("No unique characters found.")


# Example usage
input_string = "hhelloo  wwoorrlldd"
print_unique_char(input_string)

def is_list_reverse(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    first_lst_length = len(lst1)
    print(first_lst_length)
    for item in range(first_lst_length):
        if lst1[item] != lst2[first_lst_length - item - 1]:
            return False
    return True


lst1 = ['a', 'b', 'c']
lst2 = ['c', 'b', 'a']

print(is_list_reverse(lst1, lst2))


x = 1
y = 1

print(y is x)



def is_palindrome(word):
    word = word.lower().replace(" ", "")

    if word == word[::-1]:
        return True
    else:
        return False


def is_palindrome(word):
    word = word.lower().replace(" ", "")
    length = len(word)

    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False

    return True


word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 11

result = binary_search(my_list, target_value)
if result != -1:
    print(f"Found {target_value} at index {result}")
else:
    print(f"{target_value} not found in the array")



def removeElement(nums, val):
    k = 0  # Number of elements not equal to val

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


nums = [3, 2, 2, 3]
val = 3

k = removeElement(nums, val)
print("Modified nums:", nums[:k])
print("Number of elements not equal to val:", k)


def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    k = 1  # Number of unique elements

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]

k = removeDuplicates(nums)
print("Modified nums:", nums[:k])
print("Number of unique elements:", k)



def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [3, 2, 3]

majority = majorityElement(nums)
print("Majority element:", majority)


"""
A. Given list of numbers, find the largest gap between two adjacent numbers -> tell me the gap and the indexes of the 
numbers
B. Given list of numbers, find the largest gap between two any numbers -> tell me the gap and the indexes of the numbers 
C. Given list of numbers, find the largest gap between two adjacent numbers ,where the larger number appears in the 
array after the other one

"""

# A

def largest_adjacent_gap(lst: list):
    max_gap = 0
    max_gap_indexes = (0, 0)

    for i in range(len(lst) - 1):
        gap = abs(lst[i] - lst[i + 1])

        if gap > max_gap:
            max_gap = gap
            max_gap_indexes = (i, i + 1)

    return print(max_gap, max_gap_indexes)


# B
def largest_gap(lst: list):
    max_gap = 0
    max_gap_indexes = (0, 0)

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            gap = abs(lst[i] - lst[j])

            if gap > max_gap:
                max_gap = gap
                max_gap_indexes = (i, j)

    return print(max_gap, max_gap_indexes)


#C

def largest_adjacent_gap2(numbers):
    max_gap = 0
    max_gap_indexes = (0, 0)

    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            gap = numbers[i + 1] - numbers[i]

            if gap > max_gap:
                max_gap = gap
                max_gap_indexes = (i, i + 1)

    return print(max_gap, max_gap_indexes)


lst = [0, 8, 4, 0, 6, 5, 3, 22]

largest_gap(lst)

















