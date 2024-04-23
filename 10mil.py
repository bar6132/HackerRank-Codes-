# import random
#
# # Generating 10 million random balls with colors and numbers
# balls = [(random.choice(['red', 'blue', 'green', 'yellow']), random.randint(0, 9)) for _ in range(10000000)]
#
# # Initializing a dictionary to store counts for each color
# color_counts = {'red': 0, 'blue': 0, 'green': 0, 'yellow': 0}
#
# # Counting the occurrences of each color
# for color, number in balls:
#     color_counts[color] += 1
#
# # Sorting and printing the counts for each color in descending order
# sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)
#
# for color, count in sorted_colors:
#     print(f"{color.capitalize()}: {count} balls")


import random

# Generating 10 million random balls with colors, numbers, and owner names
balls = [
    {
        'color': random.choice(['red', 'blue', 'green', 'yellow']),
        'number': random.randint(0, 9),
        'owner': random.choice(['Alice', 'Bob', 'Charlie', 'David'])
    }
    for _ in range(100000)
]

# Initializing a dictionary to store counts for each owner and color
owner_color_counts = {'Alice': {'red': [0] * 10, 'blue': [0] * 10, 'green': [0] * 10, 'yellow': [0] * 10},
                      'Bob': {'red': [0] * 10, 'blue': [0] * 10, 'green': [0] * 10, 'yellow': [0] * 10},
                      'Charlie': {'red': [0] * 10, 'blue': [0] * 10, 'green': [0] * 10, 'yellow': [0] * 10},
                      'David': {'red': [0] * 10, 'blue': [0] * 10, 'green': [0] * 10, 'yellow': [0] * 10}}

# Counting the occurrences of each owner and color
for ball in balls:
    owner_color_counts[ball['owner']][ball['color']][ball['number']] += 1

# Printing the details for each owner, color, and number
for owner in owner_color_counts:
    print(f"{owner}'s balls:")

    for color in owner_color_counts[owner]:
        print(f"  {color.capitalize()} balls:")

        for number, count in enumerate(owner_color_counts[owner][color]):
            if count > 0:
                print(f"    - Ball {color} {number} ({count} {'ball' if count == 1 else 'balls'})")

    print()
