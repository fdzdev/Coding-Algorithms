# goal: Exercise 2: Reverse a String with Spaces. Ask user for input
# Input: "h e l l o"
# Output: "o l l e h"


def reverse_string_with_spaces(s):
    words = s.split(" ")  # uses slipt method!
    reversed_words = words[::-1]  # ::-1 reverses the list of words
    return " ".join(
        reversed_words
    )  # joins the list of reversed words back into a string with spaces.


# Example usage


user_input = input("Type your word brother: ")
reverse_string_with_spaces = reverse_string_with_spaces(user_input)
print(reverse_string_with_spaces)
