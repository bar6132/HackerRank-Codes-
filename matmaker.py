def print_door_mat(rows, cols):
    # Pattern for the top part of the door mat
    for i in range(1, rows, 2):
        pattern = ".|." * i
        print(pattern.center(cols, '-'))

    # Welcome message in the center
    print("WELCOME".center(cols, '-'))

    # Pattern for the bottom part of the door mat
    for i in range(rows - 2, 0, -2):
        pattern = ".|." * i
        print(pattern.center(cols, '-'))

if __name__ == "__main__":
    # Input reading
    n, m = map(int, input().split())

    # Printing the door mat
    print_door_mat(n, m)
