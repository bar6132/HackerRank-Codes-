n = int(input())
num_list = []
while n > 0:
    n = n - 1
    num_list.append(n)
for num in reversed(num_list):
    num = num**2
    print(num)