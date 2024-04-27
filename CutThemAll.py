def cutThemAll(lengths, minLength):
    # Calculate the total length of the rod by summing up all the given lengths
    rodLength = sum(lengths)
    print("Total Rod Length:", rodLength)

    # Set the current length to the total rod length
    currentLength = rodLength
    print("Initial Current Length:", currentLength)

    # Iterate through each length in the list
    for length in lengths:
        print("Processing Length:", length)

        # Check if the current length is less than the minimum required length
        if currentLength < minLength:
            # If yes, return "Impossible" because it's not possible to cut the rod into pieces of at least minLength
            print(f"Remaining Length is Less Than Minimum Length {minLength}. Cutting is Impossible.")
            return "Impossible"

        # If the current length is greater than or equal to the minimum required length, update the current length
        currentLength -= length
        print("Updated Current Length:", currentLength)

    # If the loop completes without returning "Impossible," return "Possible" because it's possible to cut the rod
    print("All Lengths Processed. Cutting is Possible.")
    return "Possible"


# Example 1
lengths = [1, 2, 3, 4]
minLength = 2
print(cutThemAll(lengths, minLength))  # prints "Possible"

# Example 2
lengths = [1, 2, 3, 4]
minLength = 5
print(cutThemAll(lengths, minLength))  # prints "Impossible"
