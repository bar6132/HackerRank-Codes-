import string

def print_rangoli(size):
    # Create a list of lowercase letters
    alphabet = string.ascii_lowercase

    # Build the rangoli
    rangoli_lines = []
    for i in range(size):
        # Create a pattern for each line
        pattern = '-'.join(alphabet[size - 1:i:-1] + alphabet[i:size])

        # Center the pattern and append to the list
        rangoli_lines.append(pattern.center(size * 4 - 3, '-'))

    # Join the lines with newline character
    print('\n'.join(rangoli_lines[::-1] + rangoli_lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
