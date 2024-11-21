# goal: Exercise 2: Reverse a String with Spaces!
# Input: "h e l l o"
# Output: "o l l e h"


def reverse_string_with_spaces(s):
    words = s.split(" ")
    reversed_words = words[::-1]
    return " ".join(reversed_words)


# Example usage
print(reverse_string_with_spaces("h e l l o"))  # Output: "o l l e h"
