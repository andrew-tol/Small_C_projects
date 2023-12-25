#!/usr/bin/env python3

# See increasing_sawtooth.png for a description of the problem.
# Written by Andrew Tol (andrew.tol777@gmail.com) in May 2020.

import sys

def inc_sawtooth(word):

    start = 0
    end = 2  # Valid minimum length for the first sequence is 2 characters.
    i = 0
    while end <= len(word):

        # Guard 1: confirm all characters in the current sequence, start : end,
        # are sorted in ascending order.
        for j in range(start, end - 1):
            if word[j] > word[j + 1]:
                return False                                    # guard failed

        # Guard 2: confirm that the last character of the currrent sequence is
        # >= the first character of the next sequence.
        if end < len(word):
            if word[end - 1] < word[end]:
                return False                                    # guard failed

        i += 1
        start = end
        end += 2 + i

    # Checking that the total number of characters is correct length
    # (Because final sequence of chars may be too long for while loop to catch)
    if start != len(word):
        return False

    return True


# This is the main entry point of the script. It checks if the script is being
# run directly (not imported).
# It then verifies that exactly one command-line argument has been provided.
# If not, it prints the correct usage of the script and exits with an error
# code. 
# Otherwise, it retrieves the first argument (assumed to be the word to check),
# calls the inc_sawtooth function with this word, and prints the boolean result.
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./increasing_sawtooth.py 'word'")
        sys.exit(1)
    
    word = sys.argv[1]
    print(inc_sawtooth(word))
